import tornado.web
from views import index
import config
import os


class Applicaiton(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/students", index.StudentsHandler),
            (r"/students2", index.Students2Handler),
            (r"/students3", index.Students3Handler),
            (r"/home", index.HomeHandler),
        ]
        super(Applicaiton, self).__init__(handlers, **config.settings)
