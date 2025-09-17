from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://"
)

@app.route('/')
@limiter.limit('10/minute; 100/hour')
def home():
    return "hello world"

if __name__ == "__main__":
    app.run(debug=True)