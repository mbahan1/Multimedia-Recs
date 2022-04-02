from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.
class Home(View):
    def get(self, request):
        return HttpResponse("MediaRecs Home")

class About(View):
    def get(self, request):
        return HttpResponse("About MediaRecs")