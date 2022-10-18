from django.urls import path
from . import views

# Pasamos los path menos la ruta admin
urlpatterns = [

    path('',views.blog, name="Blog"),
    # Pasamos por parametro el id categoria como aparece en la db
    path('categoria/<categoria_id>/', views.categoria, name="categoria"),
    
]