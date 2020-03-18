from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    MoviesListView
)
from . import views

urlpatterns = [
    path('', views.home, name='rating-home'),
    path('ratings/', views.rating, name='rating-ratings'),
    path('rating/', PostListView.as_view(), name='rating-rating'),
    path('movies/allMovies/', MoviesListView.as_view(), name='movies-home'),
    path('analysis/', views.Analysis, name='rating-analysis'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('movies/', views.movies, name='rating-movies'),
    path('profile/pwd/', views.change_password, name='rating-password'),
]