import urllib, json
from django.views import View
from django.http import JsonResponse

API_URL = "http://www.omdbapi.com/"
API_KEY = "ea9bedab"

class SearchMovie(View):
    def get(self, request, *args, **kwargs):
        searchword = self.request.GET.get('key', '')
        try:
            response = urllib.request.urlopen("%s/?s=%s&apikey=%s&page=1" % (API_URL, searchword, API_KEY))
            data = json.loads(response.read())
        except:
            data = {'Search':[]}
        return JsonResponse(data)