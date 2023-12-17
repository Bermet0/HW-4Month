from django.shortcuts import render, get_object_or_404
from . import models


# Create your views here.
def movie_list(request):
    if request.method == 'GET':
        movies = models.Movie.objects.all()
        return render(request, template_name='movies/movie_list.html',
                      context={'movie': movies})


def movie_detail(request, id):
    if request.method == 'GET':
        movie_id = get_object_or_404(models.Movie, id=id)
        return render(request, template_name='movies/movie_detail.html',
                      context={'movie_id': movie_id})
