from django.urls import path
from movie.views import SearchMovie

urlpatterns = [
    path('search/', SearchMovie.as_view(), name='search-movie')
]