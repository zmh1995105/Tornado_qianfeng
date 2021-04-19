import tornado.web
from tornado.web import RequestHandler
import json
import os
import config

class StaticFileHandler(tornado.web.StaticFileHandler):
    def __init__(self, *args, **kwargs):
        super(StaticFileHandler, self).__init__(*args, **kwargs)
        self.xsrf_token



class PCookieHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # self.set_cookie(name, value, domain, expires, path, expires_days, **kwargs)
        self.set_cookie("jason", "good")
        self.write("OK")


class GetCookieHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        cookie = self.get_cookie("jason", "logout")
        print(cookie)


class ClearCookieHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.clear_cookie("jason")
        # self.clear_all_cookies()
        self.write("OK")


class SecretCookieHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # self.set_secure_cookie(name, value, expires_days, version, **kwargs)
        self.set_secure_cookie("jason2", "good")


class GetSecretCookieHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # self.get_secure_cookie(name, value, max_age_days, min_version)
        self.get_secure_cookie("jason2")


class CookieCountHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        count = self.get_cookie("count", None)
        if not count:
            count = 1
        else:
            count = int(count)
            count += 1
        self.set_cookie("count", str(count))
        self.render("../templates/cookienum.hmtl", count=count)


class SignUpHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("../templates/login.html")

    def post(self, *args, **kwargs):
        count = self.get_cookie("count_upload", None)
        if not count:
            count = 1
        else:
            count = int(count)
            count += 1
        self.set_cookie("count_upload", str(count))


class SetXSRFHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.xsrf_token
        self.finish("OK")

class LoginHandler(RequestHandler):
    def get(self, *args, **kwargs):
        next_url = self.get_argument("next", "/")
        url = "login?next=" + next_url

        self.render("../templates/login.html", url=url)

    def post(self, *args, **kwargs):
        name = self.get_body_argument("username")
        passwd = self.get_body_argument("passwd")
        if name == "jason" and passwd == "123":
            next_url = self.get_argument("next", "/")
            self.redirect(next_url + "?flag=logon")
        else:
            next_url = self.get_argument("next", "/")
            print("next = ", next_url)
            self.redirect("/login?next=" + next_url)

class HomeHandler(RequestHandler):
    def get_current_user(self):
        flag = self.get_argument("flag")
        return flag

    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render("../templates/home.html")
