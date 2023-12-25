from django.urls import path
from . import views

urlpatterns = [
    path('movie_list/', views.movie_list, name='movie_list'),
    path('movie_list/<int:id>/', views.movie_detail, name='movie_detail'),
    path('create_movie/', views.movie_create_view, name='create_movie'),
    path('movie_list_delete/', views.movie_list_delete_view, name='movie_list_delete'),
    path('movie_drop/<int:id>/delete/', views.movie_drop_view, name='movie_drop'),
    path('movie_list_update/', views.movie_list_edit_view, name='movie_list_update'),
    path('movie_update/<int:id>/update/', views.movie_update, name='movie_update'),
    path('movie_comm/<int:id>/', views.movie_comm, name='movie_comm'),
]
