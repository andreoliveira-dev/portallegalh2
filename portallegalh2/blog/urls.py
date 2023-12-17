
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quem_somos/', views.quem_somos, name='quem_somos'),
    path('contato/', views.contato, name='contato'),
    path('duvidas/', views.duvidas, name='duvidas'),
    path('mapa/', views.mapa, name='mapa'),
    path('noticias/', views.noticias, name='noticias'),
    # Adicione outras URLs conforme necessário
]
