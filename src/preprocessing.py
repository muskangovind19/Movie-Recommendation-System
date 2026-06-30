import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)

def clean_data(df):

    columns = [
        "director",
        "cast",
        "country",
        "rating",
        "listed_in",
        "description"
    ]

    for col in columns:
        df[col] = df[col].fillna("")

    return df