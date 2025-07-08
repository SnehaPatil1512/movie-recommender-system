import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ast

@st.cache_data
def load_data():
    df = pd.read_csv("tmdb_5000_movies.csv")
    df['genres'] = df['genres'].apply(lambda x: ' '.join([i['name'] for i in ast.literal_eval(x)]))
    df['keywords'] = df['keywords'].apply(lambda x: ' '.join([i['name'] for i in ast.literal_eval(x)]))
    df['combined'] = df['genres'] + ' ' + df['keywords']
    df = df.dropna(subset=['combined']).reset_index(drop=True)
    return df

df = load_data()

@st.cache_resource
def compute_similarity(data):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(data['combined'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    indices = pd.Series(data.index, index=data['title'].str.lower())
    return cosine_sim, indices

cosine_sim, indices = compute_similarity(df)

def recommend(title, cosine_sim, indices):
    title = title.lower()
    if title not in indices:
        return ["Movie not found. Please try another."]
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices].tolist()

st.set_page_config(page_title="Movie Recommender", page_icon="🎬")

st.title("🎬 Movie Recommendation System")
st.write("Enter a movie title to get top 5 similar movies based on genres and keywords.")

user_input = st.text_input("Movie title", "")

if st.button("Recommend"):
    if user_input.strip() == "":
        st.warning("Please enter a movie title.")
    else:
        recommendations = recommend(user_input, cosine_sim, indices)
        st.subheader("Top 5 Recommended Movies:")
        for i, movie in enumerate(recommendations, 1):
            st.write(f"{i}. {movie}")
