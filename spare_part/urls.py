"""defines a url patterns for spare_part."""
from django.urls import path

from . import views

urlpatterns = [
    #homepage
    path('^$', views.index, name='index'),
]