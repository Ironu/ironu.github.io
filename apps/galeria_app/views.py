from django.shortcuts import render
from .models import *
from .forms import *


#Luego del reverse() puedo escribir entre corchetes la cantidad que quiero que se muestre EJ [:3] En ese caso se mostraran solo 3 datos 
def index(request):
    artworks = Artwork.objects.all().order_by('fecha_de_creacion').reverse()
    data = {
        'artworks': artworks
    }
    return render(request, 'index.html', data)


def sculpts(request):
    artworks = Artwork.objects.filter(categoria='1').order_by('fecha_de_creacion').reverse()
    data = {
        'artworks': artworks
    }
    return render(request, 'sculpts.html', data)

def illustrations(request):
    artworks = Artwork.objects.filter(categoria='2').order_by('fecha_de_creacion').reverse()
    data = {
        'artworks': artworks
    }
    return render(request, 'illustrations.html', data)

def tresD(request):
    artworks = Artwork.objects.filter(categoria='3').order_by('fecha_de_creacion').reverse()
    data = {
        'artworks': artworks
    }
    return render(request, '3D.html', data)

def contact(request):
    return render(request, 'contact.html')

def base(request):
    return render(request, 'base.html')

def mail(request):
    return render(request, 'mail.html')
