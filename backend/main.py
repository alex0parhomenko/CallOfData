from tornado import gen, httpclient, ioloop, queues, web
from handlers import Ping, SendMessage, DeleteMessage, Search, Index
import logging
import argparse

logging.basicConfig(filename='application.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description='oh blya')
parser.add_argument('--port', '-p', type=str, help='webserver port')
parser.add_argument('--pg_user', '-u', type=str, help='postgres user')
parser.add_argument('--dbname', '-d', type=str, help='dbname')

args = parser.parse_args()

params = dict(url='https://e.mail.ru/api/v1/messages/send',
               token='f456320fd3e17d7ba39fbb9b1087b2fd12c14db537363830',
               email='smartmail_team26@mail.ru',
               dbname=args.dbname,
               dbport=None,
               dbuser=args.pg_user)

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
    app.listen(args.port)
    ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
