
from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
import joblib

app = Flask(__name__)

from keras.models import load_model
from keras.losses import MeanSquaredError
custom_objects = {'mse': MeanSquaredError()}

from keras.saving import register_keras_serializable
@register_keras_serializable()
def mse(y_true, y_pred):
   return tf.reduce_mean(tf.square(y_true - y_pred))

# Load model & scaler
model = tf.keras.models.load_model("C:/Users/Asus/Documents/Developers_Arena_Internship_Files/Month_6_Internship_files/traffic_flow_project/traffic_flow_project/notebooks/model/lstm_model.h5", custom_objects=custom_objects)
scaler = joblib.load("C:/Users/Asus/Documents/Developers_Arena_Internship_Files/Month_6_Internship_files/traffic_flow_project/traffic_flow_project/notebooks/model/scaler.joblib")

@app.route("/")
def home():
    return "Traffic Flow Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["input"]
    data = np.array(data).reshape(1, data.shape[0], data.shape[1])
    prediction = model.predict(data)[0][0]
    return jsonify({"predicted_vehicle_count": float(prediction)})

if __name__ == "__main__":
    app.run(debug=True)
