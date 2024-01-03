from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import UpdateView
from . import models, forms
from django.urls import reverse
from django.http import HttpResponse
from .forms import ReviewForm
from django.views import generic


# Create your views here.
# def movie_list(request):
#     if request.method == 'GET':
#         movies = models.Movie.objects.all()
#         return render(request, template_name='movies/movie_list.html',
#                       context={'movie': movies})
class MovieListView(generic.ListView):
    template_name = 'movies/movie_list.html'
    model = models.Movie
    def get_queryset(self):
        return self.model.objects.all()


# def movie_detail(request, id):
#     if request.method == 'GET':
#         movie_id = get_object_or_404(models.Movie, id=id)
#         return render(request, template_name='movies/movie_detail.html',
#                       context={'movie_id': movie_id})


class MovieDetailView(generic.DetailView):
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie_id'
    def get_object(self, **kwargs):
        movie_id = self.kwargs.get('id')
        return get_object_or_404(models.Movie, id=movie_id)


# def movie_create_view(request):
#     if request.method == 'POST':
#         form = forms.MovieForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('movie_list'))
#     else:
#         form = forms.MovieForm()
#         return render(request, template_name='crud/create_movie.html',
#                       context={'form': form})


class MovieCreateView(generic.CreateView):
    template_name = 'crud/movie_create.html'
    model = models.Movie
    form_class = forms
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(MovieCreateView, self).form_valid(form=form)


def movie_list_delete_view(request):
    if request.method == 'GET':
        movies_delete = models.Movie.objects.all()
        return render(request, template_name='crud/delete/movie_list_delete.html',
                      context={'movie_delete': movies_delete})


# def movie_drop_view(request, id):
#     movie_id = get_object_or_404(models.Movie, id=id)
#     movie_id.delete()
#     # return HttpResponse('Успешно удален')
#     return redirect(reverse('movie_list_delete'))


class MovieDropView(generic.DeleteView):
    template_name = 'crud/delete/confirm_delete.html'
    success_url = 'movie_list_delete'

    def get_object(self, **kwargs):
        movie_id = self.kwargs.get('id')
        return get_object_or_404(models.Movie, id=movie_id)


def movie_list_edit_view(request):
    if request.method == 'GET':
        movies_update = models.Movie.objects.all()
        return render(request, template_name='crud/update/movie_list_update.html',
                      context={'movie_update': movies_update})


# def movie_update(request, id):
#     movie_id = get_object_or_404(models.Movie, id=id)
#     if request.method == 'POST':
#         form = forms.MovieForm(instance=movie_id, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('movie_list_update'))
#     else:
#         form = forms.MovieForm(instance=movie_id)
#         return render(request, template_name='crud/update/movie_update.html',
#                       context={
#                           "form": form,
#                           "movie_id": movie_id
#                       })


class MovieUpdateView(generic.UpdateView):
    template_name = 'crud/update/movie_list_update.html'
    form_class = forms.MovieForm
    success_url = 'movie_list_update'

    def get_object(self, **kwargs):
        movie_id = self.kwargs.get('id')
        return get_object_or_404(models.Movie, id=movie_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(MovieUpdateView, self).form_valid(form=form)


# def movie_comm(request, movie_id):
#     movie = models.Movie.objects.get(id=movie_id)
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.movie = movie
#             review.save()
#     else:
#         form = ReviewForm()
#
#     return render(request, template_name='movie_detail.html',
#                   context={
#                       'movie': movie,
#                       'form': form
#                   })


class SearchView(generic.ListView):
    template_name = 'movies/movie_list.html'
    paginate_by = 5

    def get_queryset(self):
        return models.Movie.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context
