from django.urls import path
from . import views


app_name = 'recetas'


urlpatterns = [
    path('', views.ListarRecetas, name='listar'),
]
