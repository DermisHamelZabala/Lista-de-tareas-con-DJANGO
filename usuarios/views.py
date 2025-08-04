from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import FormularioInicioSesion
from django.contrib import messages

# Create your views here.

def registro_usuario(request):

    if request.method == 'POST': # Validamos si el metodo es POST
        # pasamos los datos de la peticion
        formulario = FormularioInicioSesion(request.POST)
        # verificamos si el formulario es valido 
        if formulario.is_valid():
            # guardamos al formulario
            nuevo_formulario = formulario.save()
            # logueamos al usuario
            login(request, nuevo_formulario)
            # redirigimos al usuario 
            return redirect('lista_tareas')
        else:
            for campo, errores in formulario.errors.items():
                for error in errores:
                    messages.error(request, f"{campo}: {error}")
                        
    else: # si la peticion no es POST
        formulario = FormularioInicioSesion()
    
    context = {
        'formulario': formulario
    }

    return render(request, 'registration/registro.html', context)