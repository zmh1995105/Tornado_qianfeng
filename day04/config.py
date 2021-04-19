import os
BASE_DIRS = os.path.dirname(__file__)

options = {
    "port": 8000
}
import base64
import uuid

settings = {
    "debug": True,
    "static_path": os.path.join(BASE_DIRS, "static"),
    "templates_path": os.path.join(BASE_DIRS, "templates"),
    "cookie_secret": base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes),
    "xsrf_cookies": True,
    "login_url": "/login"
}