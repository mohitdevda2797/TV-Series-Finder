from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class SearchTerm(models.Model):
    user = models.ManyToManyField(User, blank=True)
    search_term = models.CharField(max_length=100, blank=True, null=True)
    search_date = models.DateField(blank=True, null=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.search_term


class TvSeries(models.Model):
    search_term = models.ManyToManyField(SearchTerm, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    language = models.CharField(max_length=100, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name