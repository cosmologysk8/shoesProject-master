from django.urls import path
from . import views
from .views import start_index

urlpatterns = [
    path('index/', start_index),
]