from django.shortcuts import render
from . import models


# Create your views here.
def book_view(request):
    if request.method == 'GET':
        post = models.Book.objects.all()
        return render(request, template_name='blog.html',
                      context={'post': post})
