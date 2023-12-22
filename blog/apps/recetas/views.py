from django.shortcuts import render


# Create your views here.

def ListarRecetas(request):
    return render (request, 'recetas/listar.html')