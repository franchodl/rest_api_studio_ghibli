import requests
import json

from django.shortcuts import render

# Create your views here.
def movies(request):

    context = {}

    r = requests.get('https://ghibliapi.herokuapp.com/films')

    # print(r.json()[0])

    return render(request, 'movies/movies.html', context)