from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request,'ProyectoWebApp/home.html')
    # Para probar funcionamiento cuando no habia archivo html creado.
    # return HttpResponse('Home')

def tienda(request):
    return render(request,'ProyectoWebApp/tienda.html')


