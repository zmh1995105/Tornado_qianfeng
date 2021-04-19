import tornado
from tornado.web import RequestHandler
import json
from ..model import Students
import time
from tornado.httpclient import AsyncHTTPClient
from tornado.websocket import WebSocketHandler

class HomeHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("../templates/home.html")

class ChatHandler(WebSocketHandler):
    pass


class StudentsHandler(tornado.web.RequestHandler):
    def on_response(self, response):
        if response.error:
            self.send_error(500)
        else:
            data = json.loads(response.body)
            self.write(data)
        self.finish()

    @tornado.web.asynchronous
    def get(self, *args, **kwargs):
        url = "http://127.0.0.1:8000/home"
        aClient = AsyncHTTPClient()
        aClient.fetch(url, self.on_response)
        self.write("OK")
        # s = Students("jason", 2)
        # s.save()
        # # stus = self.application.db.get_all_obj("select * from students", "students")
        # stus = Students.all()
        # print(stus)
        # self.render("../templates/student.html", stus=stus)

class Students2Handler(tornado.web.RequestHandler):

    @tornado.web.gen.coroutine
    def get(self, *args, **kwargs):
        url = "http://127.0.0.1:8000/home"
        aClient = AsyncHTTPClient()
        res = yield aClient.fetch(url)
        if res.error:
            self.send_error(500)
        else:
            data = json.loads(res)
            self.write("s2 ok")

class Students3Handler(tornado.web.RequestHandler):

    @tornado.web.gen.coroutine
    def get(self, *args, **kwargs):
        res = yield self.getData()
        self.write(res)
        self.write("s3 ok")

    @tornado.web.gen.coroutine
    def getData(self):
        url = "http://127.0.0.1:8000/home"
        aclient = AsyncHTTPClient()
        res = yield aclient.fetch(url)
        ret = {"ret": 0}
        if res.error:
            self.send_error(500)
        else:
            ret = json.loads(res)
        raise tornado.web.gen.Return(ret)