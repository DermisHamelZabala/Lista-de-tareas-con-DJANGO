from django.shortcuts import render, redirect, get_object_or_404
from .forms import TareaForm
from .models import Tarea
from django.db.models import Q

# Create your views here.

def listar_crear_tareas(request):
    busqueda = request.GET.get('buscador')

    tareas = Tarea.objects.all() # recupera todos los registro almacenados en la base de datos

    if busqueda:
        tareas = Tarea.objects.filter(
            Q(titulo__icontains = busqueda) |
            Q(estado__icontains = busqueda) 
        ).distinct()

    context = {
        'tareas': tareas,
    }

    return render(request, 'tareas/lista_tareas.html', context)

def crear_tarea(request):
    if request.method == 'POST':
        formulario = TareaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_tareas')
    else:
        formulario = TareaForm()
    
    context = {
        'formulario': formulario
    }

    return render(request, 'tareas/crear_tarea.html', context)

def actualizar_tareas(request, pk):
    tarea_actualizar = get_object_or_404(Tarea, pk=pk) # busca el id de la tarea si encuentra el registro devuelve un error 404

    if request.method == 'POST': # si la peticion es POST
        form = TareaForm(request.POST, instance = tarea_actualizar) # accede al formulario con los datos rellenos
        
        if form.is_valid(): # verifica si el formulario es valido
            form.save() # guarda el formulario
            return redirect('lista_tareas') # redirige al usuario a la pagina principal

    else: # si la peticion es GET
        form = TareaForm(instance=tarea_actualizar) # solo rellena el formulario con los datos del objecto
    
    context = {
        'formulario': form
    }

    return render(request, 'tareas/crear_tarea.html', context)


def borrar_tarea(request, pk):
    tarea_eliminar = get_object_or_404(Tarea, pk=pk)

    if request.method == 'POST':
        tarea_eliminar.delete()
        return redirect('lista_tareas')
    
    else:
        return render(request, 'tareas/eliminar_tareas.html', { 'tarea': tarea_eliminar})
    

def toggle_estado_tarea(request, pk):
    if request.method == 'POST': # verificamos si la peticion es POST
        tarea = get_object_or_404(Tarea, pk=pk) # buscamos la tarea
        tarea.estado = not tarea.estado # invertimos el valor del campo estado de tarea si es Falso lo volvemos Verdadero

        tarea.save() # guardamos nuevamente en la base de datos
        
        return redirect('lista_tareas') # redirigimos al usuario a la pagina principal