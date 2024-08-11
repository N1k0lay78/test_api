from time import time

from flask import Flask, jsonify, request, abort

app = Flask(__name__)


@app.route('/get_time', methods=['GET'])
def api_get_time():
    return jsonify({"time": time()})


@app.route('/post_time', methods=['POST'])
def api_post_time():
    if not request.json or 'time' not in request.json:
        abort(400)
    print(f"get time: {request.json['time']}")
    return jsonify({"answer": "HELLO CLIENT"})


if __name__ == '__main__':
    app.run()
