from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index, name="expenses"),
    path('add', views.add, name="add"),
]
