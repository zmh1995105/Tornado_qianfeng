import tornado.web
from db import MysqlDB

<<<<<<< HEAD

class ORM(tornado.web.RequestHandler):
    def save(self):
        table_name = (self.__class__.__name__).lower()
        field_str = value_str = "("
        for field in self.__dict__:
            field_str += (field + ",")
            if isinstance(self.__dict__[field], str):
                value_str += ("'" + self.__dict__[field] + "', ")
            else:
                value_str += (str(self.__dict__[field]) + ",")
            field_str = field_str[:-2] + ")"
            value_str = value_str[:-2] + ")"
            sql = "insert into " + table_name + " " + field_str + " values" + value_str
            print(sql)
            MysqlDB().insert(sql)
=======
class ORM(tornado.web.RequestHandler):
    def save(self):
        sql = "insert into students (name, age) values ()"
        self.application.db.insert(sql)
>>>>>>> ce9f5eb24fa85884560f5a5ec19e9976ac7e35e4

    def delete(self):
        pass

    def update(self):
        pass

<<<<<<< HEAD
    @classmethod
    def all(cls):
        table_name = cls.__name__.lower()
        sql = "select * from %s" % table_name
        db = MysqlDB()
        return db.get_all_obj(sql)

    @classmethod
    def filter(cls):
=======
    def all(self):
        pass

    def filter(self):
>>>>>>> ce9f5eb24fa85884560f5a5ec19e9976ac7e35e4
        pass
