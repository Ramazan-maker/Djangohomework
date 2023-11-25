# myapp/views.py
from django.shortcuts import render
import requests

def home(request):
    return render(request, 'myapp/base.html')

def object_card(request):
    return render(request, 'myapp/card.html')

def home(request):
    api_url = "https://jsonplaceholder.typicode.com/todos/"
    response = requests.get(api_url)
    api_data = response.json()

    context = {
        'api_data': api_data,
    }

    return render(request, 'myapp/base.html', context)