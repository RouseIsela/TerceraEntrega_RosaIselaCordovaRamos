from django.urls import include, path
from django.contrib import admin
from AppCoder import views
urlpatterns = [
    path("", views.inicio, name="Inicio"),
    path("curso", views.curso, name="Curso"),
    path("profesores", views.profesores, name="Profesores"),
    path("estudiantes", views.estudiantes, name="Estudiantes"),
    path("entregables", views.entregables, name="Entregables"),
    path("cursoFormulario",views.cursoFormulario, name="Curso"),
    path("entregableFormulario",views.entregableFormulario, name="EntregableFormulario"),
    path("estudianteFormulario",views.estudianteFormulario, name="EstudianteFormulario"),
    path("profesorFormulario",views.profesorFormulario, name="ProfesorFormulario"),
    path("busquedaCurso",views.busquedaCurso, name="BusquedaCurso"),
    path("busquedaCur/",views.busquedaCur),
    path("busquedaEstudiante",views.busquedaEstudiante, name="BusquedaEstudiante"),
    path("busquedaEst/",views.busquedaEst),
    path("busquedaProfesor",views.busquedaProfesor, name="BusquedaProfesor"),
    path("busquedaPro/",views.busquedaPro),
    path("busquedaEntregable",views.busquedaEntregable, name="BusquedaEntregable"),
    path("busquedaEntre/",views.busquedaEntre),
]
