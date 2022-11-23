from django.shortcuts import render, HttpResponse
from carro.carro import Carro

# Create your views here.

def home(request):
    carro = Carro(request)
    return render(request,'ProyectoWebApp/home.html')
    # Para probar funcionamiento cuando no habia archivo html creado.
    # return HttpResponse('Home')




