import pickle
import re
import os


def save_pickle(obj, filepath):
    """
    Save object as pickle file.
    Creates the directory if it doesn't exist.
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, "wb") as file:
        pickle.dump(obj, file)


def load_pickle(filepath):
    """
    Load pickle file.
    """
    with open(filepath, "rb") as file:
        return pickle.load(file)


def clean_text(text):
    """
    Clean text for feature engineering.
    """
    text = str(text).lower()
    text = re.sub(r"[^a-zA-Z0-9 ]", "", text)

    return text