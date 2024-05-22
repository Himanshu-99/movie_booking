import json
from django.shortcuts import render
import requests


def get_movie_data_url():
    return 'http://127.0.0.1:3000/movies/'


def movie_list(request):
    movies = []
    selected_genre = request.GET.get('genre')
    search_term = request.GET.get('search_query', '')

    try:
        url = get_movie_data_url()
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.content)


            if isinstance(data, list):

                for item in data:
                    movies.extend(item.get("movies", []))
            elif isinstance(data, dict):

                movies = data.get("movies", [])
            else:
                print(f"Warning: Unexpected data structure received from API.")

    except Exception as e:
        print(f'Error fetching data: {e}')

    if selected_genre:
        movies = [movie for movie in movies if any(genre == selected_genre for genre in movie['genre'].split(','))]

    if search_term:
        movies = [movie for movie in movies if search_term in movie['title']]

    genres = []
    for movie in movies:
        if 'genre' in movie and isinstance(movie['genre'], str):
            genres.extend(genre.strip() for genre in movie['genre'].split(','))
    genres = list(set(genres))
    context = {
        'movies': movies,
        'genres': genres,
        'selected_genre': selected_genre,
        'search_term': search_term,
    }
    return render(request, 'index.html', context)
