from django.urls import path
from . import vistas

urlpatterns = [
    path('registro/', vistas.registro, name='registro'),
]

