
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *


def start_index(request):
    shoes_list = shoes.objects.all()
    return render(request, 'index.html', {'shoes_list':shoes_list})


