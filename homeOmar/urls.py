from django.urls import path
from . import views

app_name = 'homeOmar'  # Namespace obligatorio

urlpatterns = [
    path('', views.index, name='index'),
]