import pymysql
<<<<<<< HEAD
<<<<<<<< HEAD:day03/orm/db.py
from ..config import mysql


def singleton(cls, *args, **kwargs):
    instances = {}
    def __singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return __singleton()


@singleton
class MysqlDB(object):
    host = mysql["host"]
    user = mysql["user"]
    passwd = mysql["passwd"]
    dbName = mysql["dbName"]
========
=======
>>>>>>> ce9f5eb24fa85884560f5a5ec19e9976ac7e35e4


class MysqlDB(object):
    def __init__(self, host, user, passwd, dbName):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.dbName = dbName
<<<<<<< HEAD
>>>>>>>> ce9f5eb24fa85884560f5a5ec19e9976ac7e35e4:day03/db.py
=======
>>>>>>> ce9f5eb24fa85884560f5a5ec19e9976ac7e35e4
    
    def connect(self):
        self.db = pymysql.connect(user=self.user, password=self.passwd,
                                  host=self.host, database=self.dbName)
        self.cursor = self.db.cursor()
        
    def close(self):
        self.cursor.close()
        self.db.close()
        
    def get_one(self, sql):
        res = None
        try:
            self.connect()
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
            self.close()
        except Exception as e:
            print(e)
        return res
        
    def get_all(self, sql):
        res = ()
        try:
            self.connect()
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            self.close()
        except Exception as e:
            print(e)
        return res
        
    def get_all_obj(self, sql, tableName, *args):
        resList = []
        fieldsList = []
        if len(args) > 2:
            for item in args:
                fieldsList.append(item)
        else:
          fieldsSql = "select COLUMN_NAME from information_schema.COLUMNS " \
                      "where table_name = '%s' and table_schema = '%s'" \
                      % (tableName, self.dbName)
          fields = self.get_all(fieldsSql)
          for item in fields:
              fieldsList.append(item[0])
                  
        res = self.get_all(sql)
        for item in res:
            obj = {}
            count = 0
            for i in item:
              obj[fieldsList[count]] = i
              count += 1
            resList.append(obj)
        return resList
        
    def insert(self, sql):
        return self.__edit(sql)
    
    def update(self, sql):
        return self.__edit(sql)
        
    def delete(self, sql):
        return self.__edit(sql)
        
    def __edit(self, sql):
        count = 0
        try:
            self.connect()
            count = self.cursor.execute(sql)
            self.db.commit()
            self.close()
        except Exception as e:
            print(e)
            self.db.rollback()
        return count

