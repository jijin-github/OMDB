from django.urls import path
from movie.views import SearchMovie, ListMovies, GetDetail

urlpatterns = [
    path('search/', SearchMovie.as_view(), name='search-movie'),
    path('list/', ListMovies.as_view(), name='list-movie'),
    path('details/<str:imdbID>/', GetDetail.as_view(), name='get-details')   
]