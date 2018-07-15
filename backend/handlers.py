from tornado import gen, httpclient, ioloop, queues, web
from tornado.httpclient import AsyncHTTPClient
import tornado
import urllib
import logging
import os
import json
import random
import requests
import string
from utils import add_url_params, gen_string
from db import DBConnection
import psycopg2
import psycopg2.extras
from copy import copy
from tornado.gen import multi
from multiprocessing.pool import ThreadPool

logger = logging.getLogger(__name__)
_workers = ThreadPool(10)

class Ping(web.RequestHandler):
    async def get(self):
        self.write('pong\n')
        self.finish()

class Index(web.RequestHandler):
    async def get(self):
        f = open('../index.html', 'r').read() 
        self.write(f)
        self.finish()


class SendMessage(web.RequestHandler):
    def initialize(self, url, token, email):
        self.__url = url 
        self.__token = token
        self.__email = email

    def append_params(self, data):
        data.update({"access_token": self.__token,
                     "email": self.__email})

    def avia_handler(self, data, files):
        result = random.randint(0, 1)
        extra_info = {'departure_time': '15.07.2018 01:25:41',
                      'arrive_time': '21.07.2018 02:13:33',
                      'from': 'Moscow',
                      'to': 'Kiev'}
        return False, extra_info

    def passport_handler(self, data, files):
        result = random.randint(0, 1)
        extra_info = {'name': 'Ivan',
                      'surname': 'Ivanov',
                      'sex': 'm'}
        return True, extra_info

    def apply_handlers(self, Id, data, files):
        is_avia, extra_avia = self.avia_handler(data, files)
        is_passport, extra_passport = self.passport_handler(data, files)
        with DBConnection() as conn:
            cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            cur.execute("""INSERT INTO messages VALUES (%s,%s,%s,%s,%s)""", (Id, is_passport, is_avia, json.dumps(extra_passport), json.dumps(extra_avia)))

    def upload_files(self, Id, data):
        try:
            os.mkdir("uploads")
        except:
            pass
        file_names = []
        attaches_list = []
        for k, (info,) in self.request.files.items():
            name, content_type = info['filename'], info['content_type']
            if k.find('attach') != -1:
                fname = "uploads/" + gen_string(8) + '.' + name.split('.')[-1]
                output_file = open(fname, 'wb')
                output_file.write(info['body'])
                output_file.close()
                file_names.append(fname)
                logger.debug("file " + name + " is uploaded") 

                client = AsyncHTTPClient()
                url = 'https://e.mail.ru/api/v1/messages/attaches/add'
                params = {'message_id': Id}
                self.append_params(params)
                new_url = add_url_params(url, params)
                
                 
                files = {'file': open(fname, 'rb')}
                res = requests.post(new_url, files=files)

                logger.debug(f"Upload answer {res.text}")
                attach_id = json.loads(res.text)['body']['attach']['id']
                attaches_list.append({'id': attach_id, 'type': 'attach'})
                logger.debug("file upload result: {}".format(str(res.text)))
        data.update({'attaches': {'list' : attaches_list}})
        return file_names

    async def post(self):
        data = tornado.escape.json_decode(self.get_argument('body'))
        self.append_params(data)
        Id = gen_string(32)

        filenames = self.upload_files(Id, data)
        
        data.update({"id": Id})
        logger.debug("Send message id: {}".format(data.get('id'))) 
        client = AsyncHTTPClient()
        url = add_url_params(self.__url, data)
        req = tornado.httpclient.HTTPRequest(url, body='', method='POST')
        res = await client.fetch(req)
        newId = tornado.escape.json_decode(res.body)['body']['id']

        def _callback(result):
            return 0 
        
        _workers.apply_async(self.apply_handlers, (newId, data, filenames), {}, _callback)
        #self.apply_handlers(newId, data, filenames)
        self.write(str(res.body))
        self.finish()


class DeleteMessage(web.RequestHandler):
    def initialize(self, url, token, email):
        self.__url = url
        self.__token = token
        self.__email = email

    async def post(self):
        return 0



class Search(web.RequestHandler):
    def initialize(self, url, token, email):
        self.__url = url
        self.__token = token
        self.__email = email

    async def get_message(self, Ids):
        #http(s)://domain/api/v1/messages/message
        client = AsyncHTTPClient()
        url = 'https://e.mail.ru/api/v1/messages/message'
        params = {}
        self.append_params(params)
        reqs = []
        for Id in Ids:
            curr_params = copy(params)
            curr_params.update({'id': Id})
            curr_url = add_url_params(copy(url), curr_params)
            reqs.append(tornado.httpclient.HTTPRequest(curr_url, body='', method='POST'))
        res = await multi([client.fetch(req) for req in reqs])
        tt = [tornado.escape.json_decode(item.body) for item in res]
        self.write(json.dumps(tt))
        self.finish()
 
    def append_params(self, data):
        data.update({"access_token": self.__token,
                     "email": self.__email})

    async def post(self):
        data = tornado.escape.json_decode(self.request.body)
        entity_name = data['entity']
        params = []
        for tag in data['tags']:
            attr_name = tag['attr_name']
            attr_value = tag['attr_value']
            if entity_name == 'passport':
                params.append("passport_extra_info->>'%s' = '%s'" % (attr_name, attr_value))
            elif entity_name  == 'avia':
                params.append("avia_extra_info->>'%s' = '%s'" % (attr_name, attr_value))
        with DBConnection() as conn:
            cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            p = ' OR '.join(params)
            cur.execute("""select * from messages where {};""".format(p))
            data = cur.fetchall()
        #await self.get_message(["awmRytXS"]) 
        await self.get_message([item['mid'] for item in data]) 
