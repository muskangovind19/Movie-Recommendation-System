# 🎬 Movie Recommendation System

<div align="center">

### Machine Learning Based Content Recommendation Engine


![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Recommendation%20System-green)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)
![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

</div>

---

## 📖 Project Overview

Netflix hosts thousands of movies and TV shows, making it difficult for users to find content that matches their interests. This project presents a **Content-Based Recommendation System** that recommends similar movies and TV shows based on their content characteristics.

The recommendation engine analyzes information such as:

- 🎭 Genre
- 📝 Description
- 🎬 Director
- 🎤 Cast Members
- 📅 Release Year

Using **Natural Language Processing (NLP)** and **Machine Learning**, the system identifies content similarities and recommends the most relevant titles.

---

## 🎯 Objectives

- Build an intelligent recommendation system
- Apply Natural Language Processing techniques
- Implement TF-IDF Vectorization
- Calculate similarity using Cosine Similarity
- Develop an interactive Streamlit application
- Improve content discovery for users

---

## 🏗️ System Architecture

```text
Netflix Dataset
       │
       ▼
Data Preprocessing
       │
       ▼
Feature Engineering
       │
       ▼
TF-IDF Vectorization
       │
       ▼
Cosine Similarity Matrix
       │
       ▼
Recommendation Engine
       │
       ▼
Streamlit Web Application
```

## 🚀 Features

- 🎬 Content-Based Recommendation System
- 🤖 Machine Learning Powered Recommendations
- ⚡ Fast Similarity Search
- 🎨 Interactive Streamlit Interface
- 📊 Clean and Modular Project Structure
- 🔍 Recommendation Based on Movie Metadata

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| Pandas | Data Processing |
| NumPy | Numerical Operations |
| Scikit-Learn | Machine Learning |
| Streamlit | Web Application |
| TF-IDF | Text Vectorization |
| Cosine Similarity | Recommendation Engine |
| Pickle | Model Serialization |

---

## 📊 Dataset

The project uses the Netflix Titles Dataset containing metadata about Netflix movies and TV shows.

### Features Used

- Title
- Genre
- Description
- Director
- Cast
- Release Year
- Rating

---

## ⚙️ Methodology

### 1. Data Preprocessing
- Handle missing values
- Clean textual data
- Prepare dataset for analysis

### 2. Feature Engineering
Important features such as genres, descriptions, directors, and cast members are combined into a single text feature.

### 3. TF-IDF Vectorization
The combined text is converted into numerical vectors using TF-IDF Vectorizer.

### 4. Similarity Calculation
Cosine Similarity is used to measure similarity between titles.

### 5. Recommendation Generation
The system returns the most similar movies or TV shows based on the selected title.

---

## 📂 Project Structure

```text
Netflix-Recommendation-System/
│
├── data/
│   └── netflix_titles.csv
│
├── notebooks/
│   └── EDA.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── vectorizer.py
│   ├── recommender.py
│   └── utils.py
│
├── models/
│   ├── similarity.pkl
│   └── tfidf.pkl
│
├── app/
│   ├── app.py
│   ├── recommendation.py
│   └── poster_fetcher.py
│
├── model.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🔧 Installation

### Clone the Repository

```bash
git clone https://github.com/muskangovind19/Movie-Recommendation-System.git
```

### Navigate to Project Directory

```bash
cd Netflix-Recommendation-System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

### Build Recommendation Model

```bash
python model.py
```

### Launch Streamlit Application

```bash
streamlit run app/app.py
```

---

## 📈 Future Enhancements

- Movie Poster Integration using TMDB API
- Personalized Recommendations
- Trending Content Section
- User Authentication
- AWS Cloud Deployment
- Advanced Filtering Options

---

## 🎓 Learning Outcomes

This project helped in understanding:

- Data Preprocessing
- Feature Engineering
- Natural Language Processing (NLP)
- TF-IDF Vectorization
- Cosine Similarity
- Recommendation Systems
- Streamlit Development
- End-to-End Machine Learning Projects

---
