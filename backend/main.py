#!/usr/local/bin/python3.7
from tornado import gen, httpclient, ioloop, queues, web
from handlers import Ping, SendMessage, DeleteMessage, Search, Index
import logging

logging.basicConfig(filename='application.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

params = dict(url='https://e.mail.ru/api/v1/messages/send',
               token='f456320fd3e17d7ba39fbb9b1087b2fd12c14db537363830',
               email='smartmail_team26@mail.ru')

def make_app():
    return web.Application([
        (r"/", Index),
        (r"/ping", Ping),
        (r"/send_message", SendMessage, params),
        (r"/delete_message", DeleteMessage, params),
        (r"/search", Search, params)
    ])

def main():
    app = make_app()
    app.listen(8080)
    ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
