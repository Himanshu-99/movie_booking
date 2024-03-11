import json
from django.shortcuts import render
import requests  # Import requests library

def get_movie_data_url():
    return 'http://127.0.0.1:3000/movies/'

def movie_list(request):
    movies = []
    selected_genre = request.GET.get('genre')
    try:
        url = get_movie_data_url()
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.content)
            for movie_data in data:
                movies.append({
                    'title': movie_data['movies'][0]['title'],
                    'poster': movie_data['movies'][0]['poster'],
                    'genre': ', '.join(movie_data['movies'][0]['genre']),  # Join genres as a string
                    'rating': movie_data['movies'][0]['Ratings'][0]['value'] if movie_data['movies'][0]['Ratings'] else 'N/A',
                    'year_release': int(movie_data['movies'][0]['released'].split(' ')[0]),  # Extract year from released date
                    'metacritic_rating': movie_data['movies'][0]['meta_score'] if movie_data['movies'][0]['meta_score'] else 'N/A',
                    'runtime': movie_data['movies'][0]['runtime'],
                })
    except Exception as e:
        print(f'Error fetching data: {e}')  # Log or handle error appropriately

    if selected_genre:
        movies = [movie for movie in movies if selected_genre in movie['genre']]

    genres = list(set([genre for movie in movies for genre in movie['genre'].split(',')]))
    context = {
        'movies': movies,
        'genres': genres,
        'selected_genre': selected_genre,
    }
    return render(request, 'index.html', context)
