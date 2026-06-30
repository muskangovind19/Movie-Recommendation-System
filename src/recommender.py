from sklearn.metrics.pairwise import cosine_similarity
from src.utils import save_pickle

def build_similarity(vectors):

    similarity = cosine_similarity(vectors)

    save_pickle(
        similarity,
        "models/similarity.pkl"
    )

    return similarity