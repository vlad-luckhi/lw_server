from flask import Flask, jsonify, request, make_response 
from flask_restful import Resource, Api


app = Flask(__name__)


def good(obj):
    return make_response(jsonify(obj), 200)


def bad(obj):
    return make_response(jsonify(obj), 400)


@app.route('/api/hello', methods=['GET'])
def hello():
    return make_response(jsonify({'message': 'hello',}), 200)


@app.route('/api/telegram/state', methods=['GET'])
def get_state():
    try:
        id = request.get_json()['id']
        return good({'state': id})
    except:  
        return bad({'error': 'Error converting json'})


if __name__ == '__main__':
    app.run(debug=True)