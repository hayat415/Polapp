from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.urls import path
from dbapp.views import* 

app_name="dbapp"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name="home"),
]
