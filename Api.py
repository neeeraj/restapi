from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    return jsonify({"message": f"Received: {data}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
