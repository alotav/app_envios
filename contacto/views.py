from django.shortcuts import redirect, render
from .forms import FormularioContacto
# Para el envio de correos:
from django.core.mail import EmailMessage


# Create your views here.
def contacto(request):
    # Llamamos al formulario instancuandolo y lo pasamos como parametro al template:
    formulario_contacto = FormularioContacto()

    # Si se hizo post con el formulario, obtenemos los datos enviados:
    if request.method == 'POST':
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get('nombre')
            mail = request.POST.get('mail')
            contenido = request.POST.get('contenido')

            email = EmailMessage("Mensaje desde AppEnvios-Django",
            f'El usuario {nombre} escribe lo siguiente:\n\n{contenido}',
            "",
            ["alotav.dev@gmail.com"],
            reply_to=[mail])

            try:
                email.send()
                # Redireccionamos a la misma url pasando un parametro para envio de mensaje por GET:
                return redirect('/contacto/?valido')
            except:
                return redirect('/contacto/?novalido')
        
    return render(request,'contacto/contacto.html', {'formulario_contacto': formulario_contacto})