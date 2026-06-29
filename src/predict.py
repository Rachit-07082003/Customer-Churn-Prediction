import pickle
import pandas as pd


model = pickle.load(open("models/churn_model.pkl", "rb"))


def predict(data):

    df = pd.DataFrame([data])

    prediction = model.predict(df)

    return prediction[0]