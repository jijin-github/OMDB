import urllib, json
from django.views import View
from django.http import JsonResponse
from movie.models import MovieDetails, Actor
from django.views.generic.list import ListView
from django.core import serializers
from django.conf import settings

class SearchMovie(View):
    def get(self, request, *args, **kwargs):
        searchword = self.request.GET.get('key', '')
        limit = 5
        try:
            response = urllib.request.urlopen("%s/?s=%s&apikey=%s&page=1" % (settings.API_URL, searchword, settings.API_KEY))
            data = json.loads(response.read())
        except:
            data = {'Search':[]}
        # Save details    
        if 'Search' in data:
            movies = data['Search']
            for movie in movies:
                imdbID = movie['imdbID']
                try:
                    response = urllib.request.urlopen("%s/?i=%s&apikey=%s" % (settings.API_URL, imdbID, settings.API_KEY))
                    detail_data = json.loads(response.read())
                except:
                    continue
                movie_obj, movie_obj_created = MovieDetails.objects.get_or_create(title=detail_data['Title'], 
                                        rated=detail_data['Rated'],
                                        imdbID=movie['imdbID'])
                actors = detail_data['Actors'].split(", ")                        
                if actors:
                    for actor in actors:
                        actor_obj, created = Actor.objects.get_or_create(name=actor)
                        movie_obj.actors.add(actor_obj)
        return JsonResponse(data)

class ListMovies(View):
    def get(self, request, *args, **kwargs):
        print(dir(serializers))
        data = serializers.serialize("json", MovieDetails.objects.all())
        struct = json.loads(data)
        return JsonResponse(struct, safe=False)

class GetDetail(View):
    def get(self, request, *args, **kwargs):
        imdbID = kwargs['imdbID']
        struct = []
        try:
            movie_object = MovieDetails.objects.get(imdbID=imdbID)
        except:
            movie_object = None
        if movie_object:
            data = serializers.serialize("json", [movie_object])
            struct = json.loads(data)[0]
            struct["fields"]["actors"] = list(movie_object.actors.values_list('name', flat=True))
        return JsonResponse(struct, safe=False)

        