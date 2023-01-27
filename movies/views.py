from django.http import HttpResponse
from django.views import generic

from movies.models import Director, Movie


# Create your views here.
class HomeView(generic.ListView):
    template_name = 'home.html'
    model = Director


class DirectorDetailView(generic.DetailView):
    template_name = 'director.html'
    model = Director


class MovieDetailView(generic.DetailView):
    template_name = 'movie.html'
    model = Movie
