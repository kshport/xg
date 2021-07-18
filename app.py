from flask import Flask, request
from util import XGorgon8402, XGorgon8404, XGorgon0404, XGorgon0408

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/tt/xg8404', methods=["POST"])
def tt_xgorgon8404():
    request_js = request.get_json()

    param = request_js.get('param')
    stub = request_js.get('stub')
    cookie = request_js.get('cookie')

    xg = XGorgon8404.run(param, stub, cookie)

    return xg


@app.route('/tt/xg8402', methods=["POST"])
def tt_xgorgon8402():
    request_js = request.get_json()

    param = request_js.get('param')
    stub = request_js.get('stub')
    cookie = request_js.get('cookie')

    xg = XGorgon8402.getxg(param, stub, cookie)

    return xg


@app.route('/tt/xg0404', methods=["POST"])
def tt_xgorgon0404():
    request_js = request.get_json()

    param = request_js.get('param')
    stub = request_js.get('stub')
    cookie = request_js.get('cookie')

    xg = XGorgon0404.getxg(param, stub, cookie)

    return xg


@app.route('/tt/xg0408', methods=["POST"])
def tt_xgorgon0408():
    request_js = request.get_json()

    param = request_js.get('param')
    stub = request_js.get('stub')
    cookie = request_js.get('cookie')

    xg = XGorgon0408.getxg(param, stub, cookie)

    return xg


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
