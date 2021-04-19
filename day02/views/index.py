import tornado.web
from tornado.web import RequestHandler
import json
import os
import config

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("jason is a good man")
        # 反向解析
        url = self.reverse_url("jason")
        self.write("<a href='%s'>去另一个页面</a>" % url)



class HomeHandler(tornado.web.RequestHandler):

    def initialize(self, w1, w2):
        """
        http方法之前调用
        :param w1:
        :param w2:
        :return:
        """
        self.w1 = w1
        self.w2 = w2

    def get(self, *args, **kwargs):
        self.write("home")


class Json1Handler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        per = {
            "name": "jason",
            "age": 11,
            "height": 175
        }

        # jsonStr = json.dumps(per)
        # self.set_header("Content-Type", "application/json; charset=UTF-8")
        # self.write(jsonStr)

        self.write(per)


class HeaderHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", "application/json; charset=UTF-8")

    def get(self, *args, **kwargs):
        pass


class StatusCodeHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # reason为None，则状态码必须是正常值
        # self.set_status(404)
        self.set_status(999, "this is 999")
        self.write("status code")


class RedirectHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.redirect("/")


class ErrorHandler(tornado.web.RequestHandler):
    def write_error(self, status_code: int, **kwargs):
        if status_code == 500:
            self.write("server erro")
            self.set_status(status_code)
        elif status_code == 404:
            self.write("source not found")
            self.set_status(status_code)
        else:
            self.set_status(999, "unknown")
            self.write("error unknown")

    def get(self, *args, **kwargs):
        flag = self.get_query_argument("flag")
        if flag == 0:
            # 抛出错误状态码，默认500，并且调用write_error()
            self.send_error()
        self.write("no error")

class JasonHandler(tornado.web.RequestHandler):

    def initialize(self, w1, w2):
        """
        http方法之前调用
        :param w1:
        :param w2:
        :return:
        """
        self.w1 = w1
        self.w2 = w2

    def get(self, *args, **kwargs):
        self.write("this is jason")


class CustomHandler(tornado.web.RequestHandler):
    def get(self, h1, h2, h3, *args, **kwargs):

        self.write("h1: %s, h2: %s, h3: %s" % (h1, h2, h3))

        # 若default未设置，会抛出异常
        # strip表示是否过滤两边的空白字符，默认为True
        # 如果出现同名参数，会选择最后一个参数
        self.get_query_argument("a", default=100, strip=True)

        # 同名参数
        alist = self.get_query_arguments("a")
        print(alist[0])

class SignupHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("../templates/login.html")

    def post(self, *args, **kwargs):
        username = self.get_body_argument("username")
        passwd = self.get_body_argument("password")
        hobbies = self.get_body_arguments("hobby")
        self.write("body: %s, passwrd: %s" %(username, passwd))
        self.write(hobbies[0])

        
class UploadHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("../templates/upload.html")
    
    def post(self, *args, **kwargs):
        files = self.request.files
        for filename in files.keys():
            file_arr = files[filename]
            for obj in file_arr:
                path = os.path.join(config.BASE_DIRS, "upfile", obj.filename)
                with open(path, "wb") as f:
                    f.write(obj.body)
        self.write("ok")
        


