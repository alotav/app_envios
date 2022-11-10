from django.urls import path
from . import views


# Pasamos los path menos la ruta admin
urlpatterns = [
    path('', views.tienda, name="Tienda"),
]