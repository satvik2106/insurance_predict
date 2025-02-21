from flask import Flask, request, jsonify
import numpy as np
import pickle
import tensorflow as tf

app = Flask(__name__)

# Load trained model, scaler, and encoder
model = tf.keras.models.load_model("model.h5")

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

# Route for prediction
@app.route("/api/predict", methods=["POST"])
def predict():
    try:
        data = request.json["data"]

        # Extract features
        age = float(data["age"])
        sex = data["sex"]
        bmi = float(data["bmi"])
        children = int(data["children"])
        smoker = data["smoker"]
        region = data["region"]
        expenses = float(data["expenses"])
        cibil_score = float(data["cibil_score"])

        # One-hot encode categorical data
        encoded_input = encoder.transform([[sex, smoker, region]])
        categorical_data = np.array(encoded_input).reshape(1, -1)

        # Combine numerical and categorical features
        numerical_data = np.array([[age, bmi, children, expenses, cibil_score]])
        final_input = np.concatenate([numerical_data, categorical_data], axis=1)

        # Scale data
        final_input_scaled = scaler.transform(final_input)

        # Make prediction
        prediction = model.predict(final_input_scaled)[0][0]
        prediction_label = "Prominent Customer" if prediction > 0.5 else "Not Prominent"
        return jsonify({"prediction": prediction_label})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)