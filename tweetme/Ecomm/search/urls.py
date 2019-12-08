from django.contrib import admin
from django.urls import path
from .views import Searchview

app_name="search"
urlpatterns = [
    path('', Searchview.as_view(), name='query'),

]
