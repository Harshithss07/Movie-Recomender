# 🎬 Movie Recommendation System

A smart Movie Recommendation System built using **Machine Learning** and **Python**, designed to help users discover movies they'll love based on their preferences or previously watched content.

---

## 🔍 Features

- 📌 **Content-Based Filtering** – Recommends movies based on genres, cast, director, and plot similarity.
- 📊 **Cosine Similarity / TF-IDF** – Utilizes NLP techniques for comparing movie descriptions.
- 🎯 **Search Functionality** – Find similar movies by entering the name of any movie.
- ⚡ Fast & Lightweight – Optimized for performance and quick results.
- 🧠 Optionally Integrates ML models like KNN or Collaborative Filtering.

---

## Setup
1. **Install dependencies** (globally, no venv required):
   ```sh
   pip install django pandas
   ```
2. **Run migrations:**
   ```sh
   python manage.py migrate
   ```
3. **Start the server:**
   ```sh
   python manage.py runserver
   ```

## File Structure
- `movie_list.pkl` — Pandas DataFrame with movie titles
- `similarity.pkl` — Precomputed similarity matrix
- `recommend/posters.json` — Mapping of movie titles to poster URLs
- `recommend/views.py` — Django views for home and recommendations
- `recommend/templates/recommend/home.html` — Main UI template

## Customization
- To change the number of home page posters, edit the value in `views.py` (`count >= 12`)
- To update the look, edit the CSS in `home.html`
- To add more movies or posters, update the pickle and JSON files

## Credits
- Poster images from [TMDB](https://www.themoviedb.org/)
- UI inspired by Netflix

---

Enjoy your personalized movie recommendations!
