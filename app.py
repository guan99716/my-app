import redis
from flask import Flask

app = Flask(__name__)
r = redis.Redis(host="redis", port=6379)


@app.route("/")
def hello():
    count = r.incr("hits")
    return f"這是第 {count} 次造訪\n"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
