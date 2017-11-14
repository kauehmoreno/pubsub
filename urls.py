# -- coding: utf-8 --
import tornado.web

from handlers import MainHandler

def routers():
    return tornado.web.Application([
        (r'/$', MainHandler),
    ])
