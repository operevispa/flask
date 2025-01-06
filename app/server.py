from flask import Flask, request
import numpy as np
import pickle


app = Flask(__name__)
with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)


@app.route("/predict", methods=["POST"])
def predict():
    features = request.json
    print(features)
    features = np.array(features).reshape(1, 4)

    return {"prediction": model.predict(features)[0]}


@app.route("/")
def index():
    return "Test message. The server is running"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    # app.run("localhost", 5000)
