from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context)

def about(request):
    context = {}
    return render(request, 'rango/about.html', context=context)