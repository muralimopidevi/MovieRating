from djongo import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Movies(models.Model):
    movie = models.CharField(max_length=200, null=False)
    imbdrating = models.FloatField(max_length=20, null=True)
    imbdratingcount = models.IntegerField(null=True)
    moviereleaseyear = models.IntegerField(null=True)

    def __str__(self):
        return self.movie


class Rating(models.Model):
    ratingnum = models.FloatField(max_length=20)

    def __str__(self):
        return str(self.ratingnum)


class Opinion(models.Model):
    opinionid = models.CharField(max_length=20)

    def __str__(self):
        return self.opinionid


class Post(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.SET_NULL, null=True)
    rating = models.ForeignKey(Rating, on_delete=models.SET_NULL, null=True)
    opinion = models.ForeignKey(Opinion, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.movie)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
