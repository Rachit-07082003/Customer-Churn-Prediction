import pandas as pd
from sklearn.preprocessing import LabelEncoder


def load_data(path):
    df = pd.read_csv(path)
    return df


def preprocess(df):

    df.dropna(inplace=True)

    if "customerID" in df.columns:
        df.drop("customerID", axis=1, inplace=True)

    le = LabelEncoder()

    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = le.fit_transform(df[col])

    return df