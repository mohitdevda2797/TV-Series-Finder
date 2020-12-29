from django.urls import path
# from . import views
from .api import TvSeriesSearchView
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', home_view, name='home'),
    path('tv-series-finder', search_view, name='tv-series-finder'),

    path('api/tv-series-finder', TvSeriesSearchView.as_view(), name='api-tv-series-finder'),
]
