from flask import Flask
from .settings import settings
from .extensions import init_limiter, init_redis

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = settings.SECRET_KEY
    app.config["ENV"] = settings.ENV
    init_limiter(app, settings.REDIS_URL)
    init_redis(settings.REDIS_URL)


    return app
