from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

class Rec:
    def __init__(self, title, first_aired, last_aired, genre, stream_service, img, description):
        self.title = title
        self.first_aired = first_aired
        self.last_aired = last_aired
        self.genre = genre
        self.stream_service = stream_service
        self.img = img
        self.description = description
        # self.user = user
        # self.reviews = reviews

recs = [
    Rec("Doc Martin", 2004, 2022, "Comedy", "Acorn", "https://api.rlje.net/acorn/artwork/size/docmartin_avatar?w=460", "The trials and tribulations of Dr. Martin Ellingham (Martin Clunes), a socially challenged doctor who moves from London to the picturesque village of Port Wenn in Cornwall."),
    Rec("River", 2015, 2015, "Crime", "Prime Video", "https://m.media-amazon.com/images/M/MV5BMTMyODYwOTktOGU2ZC00YjNhLThhMjQtN2MxMmYyMDQ3YzdlXkEyXkFqcGdeQXVyNTM3MDMyMDQ@._V1_.jpg", "John River is a brilliant police inspector whose genius lies side-by-side with the fragility of his mind. He is a man haunted by the murder victims whose cases he must lay to rest."),
]

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class RecList(TemplateView):
    template_name = 'recidx.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recs"] = recs
        return context