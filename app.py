from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_data():
    return jsonify({"message": "GET endpoint reached", "env_var": os.getenv('MY_ENV_VAR')}), 200

@app.route('/api', methods=['POST'])
def post_data():
    data = request.get_json()
    return jsonify({"message": "POST endpoint reached", "received_data": data}), 201

@app.route('/api/<id>', methods=['PUT'])
def update_data(id):
    data = request.get_json()
    return jsonify({"message": "PUT endpoint reached", "updated_id": id, "received_data": data}), 200

@app.route('/api/<id>', methods=['DELETE'])
def delete_data(id):
    return jsonify({"message": "DELETE endpoint reached", "deleted_id": id}), 200

if __name__ == '__main__':
    app.run(debug=True) 