from django.urls import path
from .views import listar_crear_tareas, crear_tarea, actualizar_tareas, borrar_tarea, toggle_estado_tarea

urlpatterns = [
    path('', listar_crear_tareas, name='lista_tareas'),
    path('crear-tarea/', crear_tarea, name='crear_tarea'),
    path('actualizar-tarea-<int:pk>/', actualizar_tareas, name='actualizar_tareas'),
    path('borrar-tarea-<int:pk>/', borrar_tarea, name='borrar_tarea'),
    path('estado-tarea-<int:pk>/', toggle_estado_tarea, name='toogle_estado_tarea')
]