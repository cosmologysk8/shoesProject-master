
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import shoes.models


def start_index(request):
    return render(request, 'index.html')

def get_data(request):

    my_data = shoes.models.shoes.objects.all()
    context = {
        'my_data': my_data,
    }
    return render(request, 'get_data.html', context)

