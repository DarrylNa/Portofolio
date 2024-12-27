from flask import Flask, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

with open("model/best_model.pkl", "rb") as model_file:
    best_model = pickle.load(model_file)

with open("model/scaler.pkl", "rb") as scaler_file:
    scaler = pickle.load(scaler_file)

@app.route("/", methods=["GET"])
def home():
    return "Selamat datang di API Prediksi Penyakit Jantung! Gunakan '/predict' untuk membuat prediksi."

@app.route("/predict", methods=["POST"])
def predict():
    input_data = request.json
    input_features = np.array([input_data["features"]])
    scaled_features = scaler.transform(input_features)
    prediction = best_model.predict(scaled_features)
    return jsonify({"prediction": int(prediction[0])})

if __name__ == "__main__":
    app.run(debug=True)