import os
BASE_DIRS = os.path.dirname(__file__)

options = {
    "port": 8000
}

settings = {
    "debug": True,
    "static_path": os.path.join(BASE_DIRS, "static"),
    "templates_path": os.path.join(BASE_DIRS, "templates"),
    "autoescape": None
}

mysql = {
    "host": "127.0.0.1",
    "user": "root",
    "passwd": "zmh1995105",
    "dbName": "test",
}