import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

tornado.options.define(
    name="port",
    default=8000,
    type=int,
    help="this is port")

tornado.options.define("list", default=[], type=str)

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("jason is a good man")


if __name__ == '__main__':
    tornado.options.options.logging = None
    # 转换命令行参数，并保存到tornado  option中
    # python server2.py --port=9000 --list=good,nice,handsom,cool --logging=none
    tornado.options.parse_command_line()
    print("list:", tornado.options.options.list)

    tornado.options.parse_config_file("./config")
    app = tornado.web.Application([
        (r"/", IndexHandler)
    ])

    app.listen(8000)

    # 实例化一个httpo服务器对象
    httpServer = tornado.httpserver.HTTPServer(app)
    # httpServer.listen(8000)

    # 启动多进程
    # 使用option
    httpServer.bind(tornado.options.options.port)
    # 默认单进程
    httpServer.start(5)
    # tornado.ioloop.IOLoop.current().start()
