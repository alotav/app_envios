from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label = 'Nombre', required = True, max_length= 100)
    mail = forms.CharField(label = 'Mail', required = True, max_length= 100)
    contenido = forms.CharField(label = 'Contenido', required = True, max_length= 1000, widget=forms.Textarea)