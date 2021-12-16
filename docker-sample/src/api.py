from logging import debug
from flask import Flask, jsonify

api = Flask(__name__)

@api.route('/', methods=['GET'])
async def hello_world():
     return jsonify({"message": "Hello", "status": 200}), 200

@api.errorhandler(500)
async def internal_error(error):
    return jsonify({"message": "Internal Server Error", "status": 500}), 500

@api.errorhandler(400)
async def bad_request(error):
    return jsonify({"message": "Bad Request", "status": 400}), 400

@api.errorhandler(404)
async def not_found(error):
    return jsonify({"message": "Not Found", "status": 404}), 404

if __name__ == "__main__":
    api.run(debug=True)