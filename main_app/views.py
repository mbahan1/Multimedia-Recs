from dataclasses import fields
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views import View # View class to handle requests
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect # This is our responses
from django.urls import reverse
from .models import Show, Review
from django.contrib.auth.models import User


# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class ShowList(TemplateView):
    template_name = 'show_idx.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["shows"] = Show.objects.all()
        return context