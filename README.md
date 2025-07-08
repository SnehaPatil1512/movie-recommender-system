# 🎬 Movie Recommender System

A simple content-based movie recommender system built using **Python**, **Pandas**, **Scikit-learn**, and **Streamlit**.

---

## 📌 Features

- Recommends similar movies based on genres and keywords
- Uses TF-IDF Vectorizer + Cosine Similarity
- Clean and easy Streamlit UI
- Instant top-5 recommendations

---

## 🧠 Dataset

- **TMDB 5000 Movie Dataset**  
  Source: [Kaggle - TMDB Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

File used: `tmdb_5000_movies.csv`

---

## 🚀 How to Run the App

### 1️⃣ Install dependencies

```bash
pip install streamlit pandas scikit-learn

## 2️⃣ Run the Streamlit app:

```bash
streamlit run movie_app.py

📌 Your app will open automatically in your browser at:

http://localhost:8501/

You can enter a movie title (e.g., `Avatar`) and see 5 recommended similar movies.

## 📂 Project Structure

movie_recommender_system/
├── movie_app.py               # Streamlit web app
├── movie_recommender.ipynb    # Jupyter notebook (core logic)
├── tmdb_5000_movies.csv       # Movie metadata
├── README.md                  # Project documentation (this file)
└── screenshots/               # (Optional) app interface images


## 🎥 Sample Output

**Example input:**  
`Avatar`

**Example output:**

1. Planet of the Apes  
2. Gravity  
3. Aliens  
4. Alien³  
5. Soldier


## 🛠 Libraries Used

- Python 3.10+  
- pandas  
- scikit-learn  
- streamlit

## 🙋‍♀️ Author

**Sneha Patil**  
🎓 AI/ML Internship Project

