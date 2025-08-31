from flask import Flask, request, jsonify, send_from_directory
import cv2
import numpy as np
from keras.models import load_model
from PIL import Image, ImageOps
import tensorflow as tf

app = Flask(__name__, static_folder="static")

# Suppress TensorFlow warnings
tf.get_logger().setLevel('ERROR')

# Load the model (no compilation needed for inference)
model = load_model("keras_model.h5", compile=False)

# Load the labels
class_names = open("labels.txt", "r").readlines()

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        if 'image' not in request.files:
            return jsonify({"error": "No image provided"}), 400
            
        file = request.files['image']
        
        # Read image using PIL (like Teachable Machine does)
        image = Image.open(file).convert("RGB")
        
        # Preprocess the image exactly like Teachable Machine
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
        
        # Turn the image into a numpy array
        image_array = np.asarray(image)
        
        # Normalize the image (Teachable Machine specific normalization)
        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
        
        # Create the array with the right shape
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        data[0] = normalized_image_array
        
        # Predict using the model
        prediction = model.predict(data)
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score = prediction[0][index]
        
        # Only return prediction if confidence is above threshold
        threshold = 0.5
        if confidence_score > threshold:
            # Remove the index number from the class name (e.g., "0 Hello" -> "Hello")
            label = class_name.split(' ', 1)[1].strip()
        else:
            label = "None"
        
        return jsonify({
            "prediction": label,
            "confidence": float(confidence_score)
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)