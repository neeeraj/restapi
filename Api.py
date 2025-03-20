import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    return jsonify({"message": f"Received: {data}"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # ✅ Render ke PORT variable ko use karo
    app.run(host='0.0.0.0', port=port)
