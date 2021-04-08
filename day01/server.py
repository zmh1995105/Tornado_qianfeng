import tornado.web
"""
tornado基础web框架模块
"""
import tornado.ioloop
"""
tornado核心io循环模块，封装了linux的epoll和BSD的kqueue
是tornado高效的基础
"""


class IndexHandler(tornado.web.RequestHandler):
    """
    类比Django的视图，业务处理类，用于处理get请求
    """

    def get(self, *args, **kwargs):
        self.write("jason is a good man")


if __name__ == '__main__':
    # 实例化一个app对象
    # Application是tornado web框架的和核心应用类，与服务器对应的接口，保存了路由映射表
    # listen方法用来创建一个http服务器示例，并绑定了端口
    app = tornado.web.Application([
        (r"/", IndexHandler)
    ])
    # 绑定监听端口，但是此时服务器并没有开启监听
    app.listen(8000)
    """
    tornado.ioloop: 返回当前线程的IOLoop实例
    IOLoop.start(): 启动实例的I/O循环，同时开启监听
    """
    tornado.ioloop.IOLoop.current().start()