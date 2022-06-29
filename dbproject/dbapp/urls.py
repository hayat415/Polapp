
from django.urls import path
from . views import* 

app_name="dbapp"
urlpattern= [
    path('home/', HomeView.as_view(), name="home"),
]