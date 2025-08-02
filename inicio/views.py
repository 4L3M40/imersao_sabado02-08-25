from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

def pontoturistico(request):
    return render(request, 'home/pontoturistico.html')

def galeria(request):
    return render(request, 'home/galeria.html')
# Create your views here.
