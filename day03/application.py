import tornado.web
from views import index
import config
import os
from day03.orm.db import MysqlDB


class Applicaiton(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", index.HomeHandler),
            (r"/trans", index.TransHandler),
            (r"/student", index.StudentHandler),
            (r".(.*)$", tornado.web.StaticFileHandler, {"path": os.path.join(config.BASE_DIRS, "static/html"), "default_filename": "index.html"}),

        ]
        super(Applicaiton, self).__init__(handlers, **config.settings)
        self.db = MysqlDB(**config.mysql)
