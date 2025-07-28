from django.shortcuts import render, redirect
from .forms import TareaForm
from .models import Tarea

# Create your views here.

def listar_crear_tareas(request):

    if request.method == 'POST': # si la peticion es POST
        
        form = TareaForm(request.POST) # rellenando el formulario TareaForm

        if form.is_valid(): # valida si el formulario esta relleno correctamente
            form.save() # guarda el formulario en la base de datos
            return redirect('lista_tareas') # redirige al usuario a otra pagina
    
    else: # si la peticion es GET
        form = TareaForm() # almacena un formulario vacio
    
    
    tareas = Tarea.objects.all() # recupera todos los registro almacenados en la base de datos

    context = {
        'tareas': tareas,
        'formulario': form,
    }

    return render(request, 'tareas/lista_tareas.html', context)