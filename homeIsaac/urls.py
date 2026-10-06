from django.urls import path
from . import views

app_name = 'homeIsaac'

urlpatterns = [
    path('', views.index, name='index'),
]