from django.urls import path
from .views import listar_crear_tareas

urlpatterns = [
    path('', listar_crear_tareas, name='lista_tareas')
]