#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

"""In-memory storage for users"""
users = {}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(list(users.keys()))  # Return a list of usernames


@app.route('/status', methods=['GET'])
def get_status():
    return "OK"


@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data['username']
    if username in users:
        return jsonify({"error": "Username already exists"}), 400

    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()