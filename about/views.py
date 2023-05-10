from django.shortcuts import render
from django.views.generic import ListView
from .models import About
# Create your views here.


class AboutMe(ListView):
    model = About
