from django import forms
from .models import Tarea

# creacion de la clase TareaForm que hereda de ModelForm
# para que el formulario pueda conectarse con el modelo Tarea
class TareaForm(forms.ModelForm):
    # creacion de la clase Meta para indicar a cual modelo y cuales campos usaremos
    class Meta:
        model = Tarea
        fields = [
            'titulo',
        ]