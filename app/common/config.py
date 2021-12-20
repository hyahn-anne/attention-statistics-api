import os
import json

cur_path = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(cur_path, 'config.json')
config = json.loads(open(config_path).read())
DB = config['Database']

class DBConfig:
    MYSQL_USER = DB['MYSQL_USER']
    MYSQL_PASSWORD = DB['MYSQL_PASSWORD']
    MYSQL_HOST = DB['MYSQL_HOST']
    MYSQL_PORT = DB['MYSQL_PORT']
    MYSQL_DATABASE = DB['MYSQL_DATABASE']
    DATABASE_URL = f'mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}'

db_config = DBConfig()
