from django.shortcuts import render
import folium


def index(request):
    return render(request, 'blog/index.html')


def quem_somos(request):
    return render(request, 'blog/quem_somos.html')


def contato(request):
    return render(request, 'blog/contato.html')


def duvidas(request):
    return render(request, 'blog/duvidas.html')


def mapa(request):
    return render(request, 'blog/mapa.html')


def noticias(request):
    return render(request, 'blog/noticias.html')


def mapa(request):
    return render(request, 'blog/mapa.html')
