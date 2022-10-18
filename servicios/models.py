from tabnanny import verbose
from django.db import models

# Create your models here.

# Para el uso de imagefield se necesita el modulo Pillow! istalas con pip install Pillow ;)
# Creamos la db, se creara en sqlite3: los objetos(clases) empiezan siempre en mayusculas:
class Servicio(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='servicios')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'

    def __str__(self):
        return self.titulo
