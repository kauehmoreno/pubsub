#coding:utf-8
import asyncio
import tornado.ioloop
import tornado.web

def main():
    from urls import routers
    app = routers()
    app.listen(8888)
    print(app)
    tornado.ioloop.IOLoop.configure('tornado.platform.asyncio.AsyncIOLoop')
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
