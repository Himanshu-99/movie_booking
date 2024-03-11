from django.shortcuts import render
from .models import Movie

def movie_schedule(request):
  movies = Movie.objects.all()
  selected_genre = request.GET.get('genre')
  search_term = request.GET.get('search')

  if selected_genre:
    movies = movies.filter(genre__icontains=selected_genre)

  if search_term:
    movies = movies.filter(title__icontains=search_term)

  genres = Movie.objects.values_list('genre', flat=True).distinct()
  context = {
    'movies': movies,
    'genres': genres,
    'selected_genre': selected_genre,
    'search_term': search_term,
  }
  return render(request, 'index.html', context)







