from django.shortcuts import render
from .models import Noticia


def ListarNoticias(request):
    contexto = {}


    n = Noticia.objects.all() # SELECT * FROM NOTICIAS
    contexto['noticias'] = n
   
    return render (request, 'noticias/listar.html', contexto)
