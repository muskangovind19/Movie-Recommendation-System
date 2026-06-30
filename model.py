from src.preprocessing import load_data, clean_data
from src.feature_engineering import create_tags
from src.vectorizer import create_vectors
from src.recommender import build_similarity

df = load_data(
    "data/netflix_titles.csv"
)

df = clean_data(df)

df = create_tags(df)

vectors = create_vectors(df)

similarity = build_similarity(vectors)

print("Model Built Successfully")