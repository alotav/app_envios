from django.urls import path
from ProyectoWebApp import views
# IMPORTAMOS SETTINGS Y STATIC PARA VISUALIZAR LAS IMG DESDE PANEL ADMIL:
from django.conf import settings
from django.conf.urls.static import static


# Pasamos los path menos la ruta admin
urlpatterns = [
    path('home.html', views.home, name="Home"),
    path('tienda.html/', views.tienda, name="Tienda"),
]

# AGREGAMOS ESTA LINEA PARA QUE PODAMOS VISUALIZAR IMG´S (NO ENTIENDO DEL TODO QUE HACE)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
