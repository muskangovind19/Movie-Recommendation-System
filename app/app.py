import streamlit as st
import pandas as pd
from recommendation import recommend

# ----------------------------------
# Page Configuration
# ----------------------------------
st.set_page_config(
    page_title="Netflix Recommendation System",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------
# Custom CSS
# ----------------------------------
st.markdown("""
<style>

/* App Background */
.stApp {
    background-color: #141414;
}

/* Main Container */
.block-container {
    max-width: 1400px;
    padding-top: 2rem;
    padding-bottom: 1rem;
}

/* Header */
.title {
    text-align: center;
    color: #E50914;
    font-size: 48px;
    font-weight: 800;
    margin-bottom: 8px;
}

.subtitle {
    text-align: center;
    color: #FFFFFF;
    font-size: 18px;
    margin-bottom: 30px;
}

/* Select Box */
div[data-baseweb="select"] > div {
    background-color: #222222;
    color: white;
    min-height: 50px;
    font-size: 16px;
    border-radius: 8px;
}

/* Button */
.stButton > button {
    width: 100%;
    background-color: #E50914;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 12px;
    font-size: 16px;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #ff1e28;
    color: white;
}

/* Movie Cards */
.movie-card {
    background: linear-gradient(135deg, #1f1f1f, #2d2d2d);
    color: white;
    border-radius: 12px;
    padding: 15px;
    min-height: 110px;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    font-size: 15px;
    font-weight: 600;
    margin-bottom: 15px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.5);
    transition: 0.3s;
}

.movie-card:hover {
    transform: translateY(-4px);
}

/* Footer */
.footer {
    text-align: center;
    color: gray;
    font-size: 13px;
    padding: 10px;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------
# Load Dataset
# ----------------------------------
df = pd.read_csv("data/netflix_titles.csv")

# ----------------------------------
# Header
# ----------------------------------
st.markdown("""
<div class="title">
🎬 Netflix Recommendation System
</div>
<div class="subtitle">
Discover Movies & TV Shows Similar To Your Favorites
</div>
""", unsafe_allow_html=True)

# ----------------------------------
# Sidebar
# ----------------------------------
with st.sidebar:

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/7/75/Netflix_icon.svg",
        width=100
    )

    st.markdown("## About")

    st.write("""
This recommendation system suggests similar
Movies and TV Shows using Machine Learning.
""")

    
# ----------------------------------
# Movie Selection
# ----------------------------------
selected_movie = st.selectbox(
    "🎥 Select a Movie or TV Show",
    sorted(df["title"].dropna().unique())
)

# ----------------------------------
# Recommendation Button
# ----------------------------------
if st.button("🚀 Get Recommendations"):

    with st.spinner("Finding the best recommendations..."):
        movies = recommend(selected_movie)

    st.success("Recommendations Ready!")

    st.markdown("## 🍿 Recommended For You")

    cols = st.columns(5)

    for idx, movie in enumerate(movies):

        with cols[idx%5]:

            if movie["poster"]:
                st.image(movie["poster"], use_container_width=True)
            else:
                st.image(
                    "https://via.placeholder.com/300x450?text=No+Poster",
                    use_container_width=True
            )

            st.markdown(f"### 🎬 {movie['title']}")
            st.caption(f"📺 {movie['type']}")
            st.caption(f"📅 {movie['year']}")
            st.caption(f"⭐ {movie['rating']}")

# ----------------------------------
# Footer
# ----------------------------------
st.markdown("---")

st.markdown("""
<div class="footer">
❤️ Built with Streamlit | Netflix Recommendation System
</div>
""", unsafe_allow_html=True)
