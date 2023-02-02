from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import *
from AppCoder.forms import *


"""def curso(self):
    curso= Curso(nombre="Desarrollo Web",camada="12345")
    curso.save()
    documento_de_Texto= f"-->Curso:{curso.nombre} camada {curso.camada}"
    return HttpResponse(documento_de_Texto)
"""
def inicio(request):
    return render(request,"AppCoder/inicio.html")
def curso(request):
    return render(request,"AppCoder/curso.html")
def profesores(request):
    return render(request,"AppCoder/profesores.html")
def estudiantes(request):
    return render(request,"AppCoder/estudiantes.html")
def entregables(request):
    return render(request,"AppCoder/entregables.html")
def padre(request):
    return render(request,"AppCoder/padre.html")

def cursoFormulario(request):
    if request.method == "POST":
        miformulario= CursoFormulario(request.POST)
        print(miformulario)
        if miformulario.is_valid():
            informacion=miformulario.cleaned_data
            curso= Curso(nombre=informacion["curso"],camada=informacion["camada"])
            curso.save()
            return render(request,"AppCoder/inicio.html")
    else:
        miFormulario=CursoFormulario()
    return render(request, "AppCoder/cursoFormulario.html",{"miFormulario": miFormulario})

def entregableFormulario(request):
    if request.method == "POST":
        miformulario= EntregableFormulario(request.POST)
        print(miformulario)
        if miformulario.is_valid():
            informacion=miformulario.cleaned_data
            curso= Entregable(nombre=informacion["nombre"],fecha_de_entrefa=informacion["fecha_de_entrega"],entregado=informacion["entregado"])
            curso.save()
            return render(request,"AppCoder/inicio.html")
    else:
        miFormulario=EntregableFormulario()
    return render(request, "AppCoder/cursoFormulario.html",{"miFormulario": miFormulario})
def estudianteFormulario(request):
    if request.method == "POST":
        miformulario= EstudianteFormulario(request.POST)
        print(miformulario)
        if miformulario.is_valid():
            informacion=miformulario.cleaned_data
            curso= Estudiante(nombre=informacion["nombre"],apellido=informacion["apellido"],email=informacion["email"])
            curso.save()
            return render(request,"AppCoder/inicio.html")
    else:
        miFormulario=EstudianteFormulario()
    return render(request, "AppCoder/cursoFormulario.html",{"miFormulario": miFormulario})
def profesorFormulario(request):
    if request.method == "POST":
        miformulario= ProfesorFormulario(request.POST)
        print(miformulario)
        if miformulario.is_valid():
            informacion=miformulario.cleaned_data
            curso= Profesor(nombre=informacion["nombre"],apellido=informacion["apellido"],email=informacion["email"],profesion=informacion["profesion"])
            curso.save()
            return render(request,"AppCoder/inicio.html")
    else:
        miFormulario=ProfesorFormulario()
    return render(request, "AppCoder/cursoFormulario.html",{"miFormulario": miFormulario})
def busquedaCurso(request):
    return render(request,"AppCoder/busquedaCurso.html")
def busquedaCur(request):
   # respuesta=f"Estoy buscando la camda nro: {request.GET['camada']}"
   if request.GET["camada"]:
       camada= request.GET['camada']
       cursos= Curso.objects.filter(camada__icontains=camada)
    #return HttpResponse(respuesta)
       return render(request,"AppCoder/resulbusquedaCurso.html",{"cursos":cursos,"camada":camada})
   else:
       respuesta="No enviaste los datos"
       return HttpResponse(respuesta)
def busquedaEstudiante(request):
    return render(request,"AppCoder/busquedaEstudiante.html")
def busquedaEst(request):
   # respuesta=f"Estoy buscando la camda nro: {request.GET['camada']}"
   if request.GET["id"]:
       id= request.GET['id']
       estudiantes= Estudiante.objects.filter(id__icontains=id)
    #return HttpResponse(respuesta)
       return render(request,"AppCoder/resulbusquedaEstudiante.html",{"estudiantes":estudiantes,"id":id})
   else:
       respuesta="No enviaste los datos"
       return HttpResponse(respuesta)
def busquedaProfesor(request):
    return render(request,"AppCoder/busquedaProfesor.html")
def busquedaPro(request):
   # respuesta=f"Estoy buscando la camda nro: {request.GET['camada']}"
   if request.GET["id"]:
       id= request.GET['id']
       profesores= Profesor.objects.filter(id__icontains=id)
    #return HttpResponse(respuesta)
       return render(request,"AppCoder/resulbusquedaProfesor.html",{"profesores":profesores,"id":id})
   else:
       respuesta="No enviaste los datos"
       return HttpResponse(respuesta)
def busquedaEntregable(request):
    return render(request,"AppCoder/busquedaEntregable.html")
def busquedaEntre(request):
   # respuesta=f"Estoy buscando la camda nro: {request.GET['camada']}"
   if request.GET["id"]:
       id= request.GET['id']
       entregables= Entregable.objects.filter(id__icontains=id)
    #return HttpResponse(respuesta)
       return render(request,"AppCoder/resulbusquedaEntregable.html",{"entregables":entregables,"id":id})
   else:
       respuesta="No enviaste los datos"
       return HttpResponse(respuesta)