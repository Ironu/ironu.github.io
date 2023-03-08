from django.shortcuts import render
from .models import *



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

def images(request):
    artworks = Artwork.objects.filter(categoria='2').order_by('fecha_de_creacion').reverse()
    data = {
        'artworks': artworks
    }
    return render(request, 'images.html', data)

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

def EP(request):
    return render(request, 'EP.html')
