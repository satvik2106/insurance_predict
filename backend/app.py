from flask import Flask, jsonify
from flask_cors import CORS
from routes import routes_bp  # Import routes

app = Flask(__name__)

# CORS Configuration (Allow requests from frontend)
CORS(app, origins="http://localhost:3000")

# Configure MongoDB (if using Flask-S   QLAlchemy or PyMongo, adjust accordingly)


# Register Blueprints (API Routes)
app.register_blueprint(routes_bp, url_prefix="/api")

# Root Route
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Insurance Prediction API!"})

# Print all routes registered with Flask
for rule in app.url_map.iter_rules():
    print(rule)


# Run Server
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

# from flask import Flask, request, jsonify
# import numpy as np
# import tensorflow as tf

# app = Flask(__name__)

# # Load your model (Ensure correct path)
# model = tf.keras.models.load_model("./model/model.h5")

# @app.route('/api/predict', methods=['GET','POST'])
# def predict():
#     try:
#         data = request.get_json()
#         features = np.array(data["features"]).reshape(1, -1)

#         # Ensure correct input shape
#         if features.shape[1] != 10:
#             return jsonify({"error": "Invalid input shape"}), 400

#         prediction = model.predict(features)
#         is_prominent = prediction[0][0] > 0.5  # Adjust threshold

#         return jsonify({"prominent": is_prominent})

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)