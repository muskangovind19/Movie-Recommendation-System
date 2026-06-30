from sklearn.feature_extraction.text import TfidfVectorizer
from src.utils import save_pickle

def create_vectors(df):

    tfidf = TfidfVectorizer(
        stop_words="english",
        max_features=5000
    )

    vectors = tfidf.fit_transform(df["tags"])

    save_pickle(
        tfidf,
        "models/tfidf.pkl"
    )

    return vectors