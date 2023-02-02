from django import forms
class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()
class EntregableFormulario(forms.Form):
    nombre =forms.CharField(max_length=40)
    fecha_de_entrega= forms.DateField()
    entregado=forms.BooleanField()
class EstudianteFormulario(forms.Form):
    nombre =forms.CharField(max_length=40)
    apellido= forms.CharField(max_length=40)
    email=forms.EmailField()
class ProfesorFormulario(forms.Form):
    nombre =forms.CharField(max_length=40)
    apellido= forms.CharField(max_length=40)
    email=forms.EmailField()
    profesion=forms.CharField(max_length=30)