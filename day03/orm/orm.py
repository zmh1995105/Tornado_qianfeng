import tornado.web
from db import MysqlDB

class ORM(tornado.web.RequestHandler):
    def save(self):
        sql = "insert into students (name, age) values ()"
        self.application.db.insert(sql)

    def delete(self):
        pass

    def update(self):
        pass

    def all(self):
        pass

    def filter(self):
        pass
