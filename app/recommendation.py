import sys
import os
import pandas as pd
from poster_fetcher import fetch_poster

# Add project root to Python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.utils import load_pickle

# Load dataset
df = pd.read_csv(
    os.path.join(project_root, "data", "netflix_titles.csv")
)

# Load similarity matrix
similarity = load_pickle(
    os.path.join(project_root, "models", "similarity.pkl")
)


def recommend(movie_name):
    try:
        movie_index = df[df["title"] == movie_name].index[0]

        distances = similarity[movie_index]

        movie_list = sorted(
            list(enumerate(distances)),
            key=lambda x: x[1],
            reverse=True
        )[1:6]

        recommendations = []

        for movie in movie_list:

            movie_data = df.iloc[movie[0]]

            recommendations.append({
                "title": movie_data["title"],
                "poster": fetch_poster(movie_data["title"]),
                "type": movie_data["type"],
                "year": movie_data["release_year"],
                "rating": movie_data["rating"]
            })

        return recommendations

    except Exception as e:
        print(e)
        return []