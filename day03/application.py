import tornado.web
from views import index
import config
import os

class Applicaiton(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", index.HomeHandler),
            (r"/trans", index.TransHandler),
            (r".(.*)$", tornado.web.StaticFileHandler, {"path": os.path.join(config.BASE_DIRS, "static/html"), "default_filename": "index.html"}),
            (r"/student", index.StudentHandler)
    
   
        ]
        super(Applicaiton, self).__init__(handlers, **config.settings)

