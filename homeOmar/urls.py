from django.urls import path
from . import views

app_name = 'homeOmar'

urlpatterns = [
    path('', views.index, name='index'),
]