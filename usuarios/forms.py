from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormularioInicioSesion(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
        )