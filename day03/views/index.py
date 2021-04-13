import tornado.web
from tornado.web import RequestHandler
import json


class HomeHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        temp = 100
        per = {
            "name": "jason",
            "age": 19
        }
        flag = 0
        
        stus = [
            {
                "name": "a",
                "age": 21
            },
            {
                "name": "b",
                "age": 11
            }
        ]
        self.render("../templates/home.html", num = temp, per = per, flag = flag, stus = stus)
        

class TransHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs): 
        str = "<h1>jason is a good man.</h1>"

        self.render("../templates/trans.html", str=str)
        
class StudentHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs): 
        stus = []
        self.render("student.html", stus=stus)

