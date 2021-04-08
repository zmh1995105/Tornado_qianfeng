import tornado.web
import tornado.ioloop
import tornado.httpserver


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("jason is a good man")


if __name__ == '__main__':

    app = tornado.web.Application([
        (r"/", IndexHandler)
    ])

    app.listen(8000)

    # 实例化一个httpo服务器对象
    httpServer = tornado.httpserver.HTTPServer(app)
    # httpServer.listen(8000)

    # 启动多进程
    httpServer.bind(8000)
    # 默认单进程
    httpServer.start(5)
    # tornado.ioloop.IOLoop.current().start()
