from django.urls import path
from contacto import views

# IMPORTAMOS SETTINGS Y STATIC PARA VISUALIZAR LAS IMG DESDE PANEL ADMIL:
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.contacto, name="Contacto"),
]