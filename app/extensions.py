from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import redis


def init_limiter(app, storage_uri):
    global limiter
    limiter = Limiter(key_func=get_remote_address, storage_uri=storage_uri)
    limiter.init_app(app) #links the limiter to our app 
    return limiter

def init_redis(url):
    global r
    r = redis.Redis.from_url(url, decode_response=True)
    return r