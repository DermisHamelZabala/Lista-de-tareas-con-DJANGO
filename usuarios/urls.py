from django.urls import path, include
from .views import registro_usuario

urlpatterns = [
    path('registro-usuario/', registro_usuario, name='registro'),
    path('', include('django.contrib.auth.urls')),
]