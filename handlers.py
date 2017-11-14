#coding:utf-8
import json
from tornado.web import RequestHandler, asynchronous

class MainHandler(RequestHandler):

    @asynchronous
    def get(self, *args, **kwargs):
        self.set_header('Content-Type', 'application/json')
        items = {'name': 'Client2'}

        self.write(json.dumps(items))
        self.finish()
