import tornado.ioloop
import tornado.httpserver
import tornado.options
import config
from application import Applicaiton


if __name__ == '__main__':

    app = Applicaiton()
    # 实例化一个http服务器对象
    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.bind(config.options["port"])
    # 默认单进程
    httpServer.start(1)
    tornado.ioloop.IOLoop.current().start()
