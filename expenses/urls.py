from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="expenses"),
    path('add', views.index, name="add"),
]