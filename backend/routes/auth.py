from flask import Blueprint, request, jsonify
from pymongo import MongoClient

auth_bp = Blueprint("auth", __name__)

# MongoDB client setup
client = MongoClient("mongodb://localhost:27017/")
db = client["insurance"]
users_collection = db["users"]

@auth_bp.route("/signup", methods=["POST"])
def signup():
    try:
        data = request.json
        if "username" not in data or "password" not in data:
            return jsonify({"error": "Missing username or password"}), 400

        existing_user = users_collection.find_one({"username": data["username"]})
        if existing_user:
            return jsonify({"error": "Username already exists"}), 400

        users_collection.insert_one({"username": data["username"], "password": data["password"]})
        return jsonify({"message": "User created successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@auth_bp.route("/login", methods=["POST"])
def login():
    try:
        data = request.json
        if "username" not in data or "password" not in data:
            return jsonify({"error": "Missing username or password"}), 400

        user = users_collection.find_one({"username": data["username"]})
        if not user or user["password"] != data["password"]:
            return jsonify({"error": "Invalid credentials"}), 400

        return jsonify({"message": "Login successful"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
