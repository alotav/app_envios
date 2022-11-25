from .import views2
from django.urls import path


urlpatterns = [
    
    path('', views2.procesar_pedido, name="procesar_pedido"),
    
]