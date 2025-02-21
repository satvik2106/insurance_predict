import os
from flask import Blueprint, request, jsonify
from pymongo import MongoClient
import tensorflow as tf
import numpy as np

predict_bp = Blueprint("predict", __name__)

# Get the absolute path to model.h5
MODEL_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../model/model.h5"))

# Load the model
model = tf.keras.models.load_model(MODEL_PATH)

# MongoDB client setup (make sure you have MongoDB running locally or in your environment)
# Update MongoDB URI if needed (it should point to your MongoDB instance)
MONGO_URI = "mongodb://localhost:27017/"  # You can replace this with your MongoDB URI if it's hosted elsewhere
client = MongoClient(MONGO_URI)

# Connect to your specific database and collection
db = client["insurance"]  # Replace with your database name
details_collection = db["users"]  # Replace with your collection name

@predict_bp.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json.get("data")
        if not data:
            return jsonify({"error": "Invalid input data"}), 400

        # Extract and format data from the request
        input_values = np.array([[float(data["age"]), float(data["bmi"]), int(data["children"]), float(data["expenses"]), float(data["cibil_score"]), 0, 0, 0, 0, 0]])

        # Make the prediction
        prediction = model.predict(input_values)

        # Optionally, save prediction to MongoDB (or use for other tasks)
        prediction_data = {
            "age": data["age"],
            "bmi": data["bmi"],
            "children": data["children"],
            "expenses": data["expenses"],
            "cibil_score": data["cibil_score"],
            "prediction": float(prediction[0][0])
        }
        details_collection.insert_one(prediction_data)  # Save the prediction data into MongoDB

        return jsonify({"prediction": float(prediction[0][0])}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
