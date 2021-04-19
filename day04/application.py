import tornado.web
from views import index
import config
import os

class Applicaiton(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/pcookie", index.PCookieHandler),
            (r"/(.*)$", index.StaticFileHandler,
             {"path": os.path.join(config.BASE_DIRS, "static/html"),
              "default_filename": "index.html"}),

            ("/login", index.LoginHandler),
            ("/home", index.HomeHandler)


        ]
        super(Applicaiton, self).__init__(handlers, **config.settings)


