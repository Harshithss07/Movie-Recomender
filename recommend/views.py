
from django.shortcuts import render

import pickle
import os
import json
from django.views.decorators.csrf import csrf_exempt

# Load models and posters once at startup
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(os.path.join(BASE_DIR, 'movie_list.pkl'), 'rb') as f:
    movies = pickle.load(f)
with open(os.path.join(BASE_DIR, 'similarity.pkl'), 'rb') as f:
    similarity = pickle.load(f)
with open(os.path.join(BASE_DIR, 'recommend', 'posters.json'), 'r', encoding='utf-8') as f:
    posters = json.load(f)

def home(request):
    # Pass all movie titles for search suggestions
    movie_titles = movies['title'].tolist()
    # Show a random selection of 12 posters on the home screen
    import random
    all_movies = movies['title'].tolist()
    random.shuffle(all_movies)
    home_posters = []
    count = 0
    for title in all_movies:
        poster_url = posters.get(title, '')
        if poster_url:
            home_posters.append({'title': title, 'poster': poster_url})
            count += 1
        if count >= 12:
            break
    return render(request, 'recommend/home.html', {'movie_titles': movie_titles, 'home_posters': home_posters})

@csrf_exempt
def recommend_movie(request):
    recommendations = []
    error = None
    movie_titles = movies['title'].tolist()
    home_posters = []
    if request.method == 'POST':
        movie_name = request.POST.get('movie')
        try:
            # Find the index of the movie
            idx = movies[movies['title'].str.lower() == movie_name.strip().lower()].index[0]
            sim_scores = list(enumerate(similarity[idx]))
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
            top_indices = [i[0] for i in sim_scores[1:6]]
            for i in top_indices:
                title = movies['title'].iloc[i]
                poster_url = posters.get(title, '')
                recommendations.append({'title': title, 'poster': poster_url})
        except Exception as e:
            error = 'Movie not found or error in recommendation.'
    return render(request, 'recommend/home.html', {'recommendations': recommendations, 'error': error, 'movie_titles': movie_titles, 'home_posters': home_posters})
