import tornado.web
from tornado.web import RequestHandler
import json
from ..model import Students

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
        str = "<h1>jason is a 12312good man.</h1>"

        self.render("../templates/trans.html", str=str)


class StudentHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        s = Students("jason", 2)
        s.save()
        # stus = self.application.db.get_all_obj("select * from students", "students")
        stus = Students.all()
        print(stus)
        self.render("../templates/student.html", stus=stus)

