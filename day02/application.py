import tornado.web
from views import index
import config


class Applicaiton(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", index.IndexHandler),
            (r"/home", index.HomeHandler, {"w1": "good", "w2": "nice"}),
            (r"/json1", index.Json1Handler),
            (r"/header", index.HeaderHandler),
            (r"/status", index.StatusCodeHandler),
            # redirect
            (r"/index", index.RedirectHandler),
            (r"/error", index.ErrorHandler),
            # 反向解析
            tornado.web.url(r"/jason", index.JasonHandler, {"w1": "good", "w2": "nice"},
                            name="jason"),
            (r"/custom/(?P<h1>\w+)/(?P<h3>\w+)/(?P<h2>\w+)", index.CustomHandler),
            (r"/signup", index.SignupHandler),
            (r"/upload", index.UploadHandler)

        ]
        super(Applicaiton, self).__init__(handlers, **config.settings)

