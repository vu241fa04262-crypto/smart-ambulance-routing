import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import os

MODEL_PATH = "traffic_model.pkl"

def train_model():
    data = pd.read_csv("data/traffic.csv")

    X = data[['hour', 'day']]
    y = data['traffic']

    model = LinearRegression()
    model.fit(X, y)

    pickle.dump(model, open(MODEL_PATH, "wb"))

def predict_traffic(hour, day):
    model = pickle.load(open(MODEL_PATH, "rb"))
    return model.predict([[hour, day]])[0]