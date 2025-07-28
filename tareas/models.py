from django.db import models

# Create your models here.

class Tarea(models.Model):
    # campo titulo para almacenar el titulo de la tarea
    titulo = models.CharField(max_length=200)
    # campo estado para guardar el estado (no completa, completa) de la tarea
    estado = models.BooleanField(default=False)
    # campo fecha de creacion para guarda la fecha en la que se creo la tarea
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    # metodo __str__ para hacer legible los registro en el administrador de django
    def __str__(self):
        return self.titulo
    
    # clase Meta para ordenar por mas recientes las tareas
    class Meta:
        ordering = [
            '-fecha_creacion'
        ]