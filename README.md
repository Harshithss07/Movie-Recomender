# Movie Recommendation System

A Netflix-inspired movie recommendation web app built with Django. Users can search for a movie and get personalized recommendations based on similarity, or browse a visually engaging home page with popular movie posters.

## Features
- Modern, responsive UI inspired by Netflix
- Search for any movie and get 5 similar recommendations
- Movie posters displayed for all recommendations
- Autocomplete search suggestions
- Random popular movies shown on the home page
- Epic animated background for a cinematic feel

## How It Works
- Movie data and similarity matrix are precomputed and loaded from `movie_list.pkl` and `similarity.pkl`
- Poster URLs are loaded from `posters.json`
- The backend uses pandas for fast lookups and similarity scoring
- The frontend is styled with custom CSS for a streaming-service look

## Handling Large Model Files

**Note:** The model/data files (`movie_list.pkl`, `similarity.pkl`, and `recommend/posters.json`) are large and should NOT be committed to git. They are included in `.gitignore`.

- If you are sharing this project, provide these files via cloud storage (Google Drive, Dropbox, etc.) or direct download links.
- If you need to generate them, document the process or provide scripts.

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
4. **Open your browser:**
   Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

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
