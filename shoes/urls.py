from django.urls import path
from . import views
from .views import start_index
from .views import get_data

urlpatterns = [
    path('index/', start_index),
    path('get_data/', get_data, name='get_data'),
]