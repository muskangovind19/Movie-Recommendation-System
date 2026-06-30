import requests

API_KEY = "e3aaf986"


def fetch_poster(movie_name):
    url = f"https://www.omdbapi.com/?t={movie_name}&apikey={API_KEY}"

    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        if (
            data.get("Response") == "True"
            and data.get("Poster")
            and data["Poster"] != "N/A"
        ):
            return data["Poster"]

    except Exception:
        pass

    return "https://via.placeholder.com/300x450?text=No+Poster"