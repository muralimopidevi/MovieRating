from collections import Counter
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .filters import PostFilter, MovieFilter
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Movies, Opinion, Rating
import pandas as pd


def home(request):
    query_movies = list(Movies.objects.values())
    query_post = list(Post.objects.values())
    query_user = list(User.objects.values())
    query_movies = pd.DataFrame(query_movies)
    query_post = pd.DataFrame(query_post)
    query_user = pd.DataFrame(query_user)
    # analysis count cards
    movies_count = query_movies['id'].count()
    post_count = query_post['id'].count()
    user_count = query_user['id'].count()
    context = {
        'title': 'home',
        'movies_count': movies_count,
        'post_count': post_count,
        'user_count' : user_count,
    }
    return render(request, 'rating/home.html', context)


def rating(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'title'
    }
    return render(request, 'rating/ratings.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'rating/ratings.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class UserPostListView(ListView):
    model = Post
    template_name = 'rating/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['movie', 'rating', 'opinion', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['movie', 'rating', 'opinion', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def movies(request):
    moviess = Movies.objects.all()
    context = {
        'moviess': moviess,
        'title': 'Movies',
    }
    return render(request, 'rating/moviesinfo.html', context)


class MoviesListView(ListView):
    model = Movies
    template_name = 'rating/moviesinfo.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'moviess'
    ordering = ['-moviereleaseyear']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = MovieFilter(self.request.GET, queryset=self.get_queryset())
        return context


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, f'Your password was successfully updated!')
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'rating/password.html', {
        'form': form
    })


def Analysis(request):
    # Connections
    query_movies = list(Movies.objects.values())
    query_post = list(Post.objects.values())
    query_user = list(User.objects.values())
    query_movies = pd.DataFrame(query_movies)
    query_post = pd.DataFrame(query_post)
    query_user = pd.DataFrame(query_user)
    # analysis count cards
    movies_count = query_movies['id'].count()
    post_count = query_post['id'].count()
    user_count = query_user['id'].count()

    # Doughnut chart for OPINION'S
    label_opinion = []
    data_opinion = []
    queryset_opinion = Post.objects.order_by('-opinion')
    for city in queryset_opinion:
        data_opinion.append(city.opinion.opinionid)

    cnt_opinion = Counter(data_opinion)
    labels_opinion = list(cnt_opinion.keys())
    data_opinion = list(cnt_opinion.values())

    # Bar chart for Rating's Count
    label_rating = []
    data_rating = []
    queryset_rating = Post.objects.order_by('-rating')
    for city in queryset_rating:
        data_rating.append(city.rating.ratingnum)

    cnt_rating = Counter(data_rating)
    labels_rating = list(cnt_rating.keys())
    data_rating = list(cnt_rating.values())

    # Line chart for Movies Year Count
    label_movie = []
    data_movie = []
    data_movie_yr =[]
    data_movie_imbd = []
    data_movie_user = []

    queryset_movie = Post.objects.order_by('-date_posted')[:10]
    for city in queryset_movie:
        data_movie.append(city.movie.movie)
        data_movie_yr.append(city.movie.moviereleaseyear)
        data_movie_imbd.append(city.movie.imbdrating)
        data_movie_user.append(city.author.username)

    cnt_movie = Counter(data_movie)
    labels_movie = list(cnt_movie.keys())
    data_movie = list(cnt_movie.values())

    cnt_movie_yr = Counter(data_movie_yr)
    labels_movie_yr = list(cnt_movie_yr.keys())
    data_movie_yr = list(cnt_movie_yr.values())

    cnt_movie_imbd = Counter(data_movie_imbd)
    labels_movie_imbd = list(cnt_movie_imbd.keys())
    data_movie_imbd = list(cnt_movie_imbd.values())

    cnt_movie_user = Counter(data_movie_user)
    labels_movie_user = list(cnt_movie_user.keys())
    data_movie_user = list(cnt_movie_user.values())

    context = {
        'title': 'Analysis',
        'movies_count': movies_count,
        'post_count': post_count,
        'user_count': user_count,
        'labels_opinion': labels_opinion,
        'data_opinion': data_opinion,
        'labels_rating': labels_rating,
        'data_rating': data_rating,
        'labels_movie': labels_movie,
        'data_movie': data_movie,
        'labels_movie_yr': labels_movie_yr,
        'data_movie_yr': data_movie_yr,
        'labels_movie_imbd': labels_movie_imbd,
        'data_movie_imbd': data_movie_imbd,
        'labels_movie_user': labels_movie_user,
        'data_movie_user': data_movie_user,
    }
    return render(request, 'rating/Analysis.html', context)
