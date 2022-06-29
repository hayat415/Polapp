from webbrowser import get
from django.shortcuts import render
from django.views.generic import View
from .models import Interest, Person, PersonAddress, City



class HomeView(View):
    def get( request, *args, **kwargs):
        print("I am in the get method")


        context={}
        return render (request, "home.html", context)
# Create your views here.
