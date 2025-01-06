import requests
import numpy as np


def nums():
    res = requests.post("http://localhost:5000/add", json={"num": 9})

    print(f"Status code {res.status_code}")

    if res.status_code == 200:
        print(res.json()["result"])
    else:
        print(res.text)


def predict():
    features = [1, 1, 1, 0.661212487096872]
    # для тестирования FLASK сервера, который по умолчанию поднимается на порту 5000
    # res = requests.post("http://localhost:5000/predict", json=features)
    # для тестирования FLASK + UWSGI + NGINX, который поднимает на порту 80, который является портом по умолчанию
    res = requests.post("http://localhost/predict", json=features)

    print(f"Status code {res.status_code}")

    if res.status_code == 200:
        print(res.json()["prediction"])
    else:
        print(res.text)


if __name__ == "__main__":
    predict()
