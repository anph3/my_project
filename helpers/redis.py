import redis
import importlib
from configs import app
import json
import os

sys_conf = importlib.import_module("enviroments."+os.getenv('APP_ENV'))

class CacheRedis():
    def __init__(self, connection='default'):
        self.r = redis.Redis(host=sys_conf.REDIS_HOST, port=sys_conf.REDIS_PORT, db=sys_conf.REDIS_DB)

    def get_auth_data(
        self, key, prefix = app.Token.session_prefix.value
    ):
        data = self.r.get(prefix+str(key))
        if data is None:
            return data
        data = data.decode("UTF-8").replace("'", '"')
        return json.loads(data)
    
    def check_auth_data(
        self, key, prefix = app.Token.session_prefix.value
    ):
        return self.r.get(prefix+str(key))