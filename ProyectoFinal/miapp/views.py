from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from miapp.models import Curso
from django.db.models import Q


# Create your views here.
layout = """
    <h1> Examen Final (LP3) || Gerardo Castillo </h1>
    <hr/>
    <ul>
        <li>
            <a href="/Cusrsos">Cusrsos</a>
        </li>
        <li>
            <a href="/CrearCurso">Crear Curso</a>
        </li>
        <li>
            <a href="/Carreras">Carreras</a>
        </li>
        <li>
            <a href="/Crear Carrera">Crear Carrera </a>
        </li>
    </ul>
    <hr/>
"""

def index(request):
      
    return render(request, 'Index.html', {
        'titulo': 'Inicio',
        'mensaje': 'Listado de Cursos',
    })

def crear_curso(request):
    return render(request, 'crear_curso.html')

def save_curso(request):
    if request.method == 'POST':
        codigo = request.POST['codigo']
        nombre = request.POST['nombre']
        horas = request.POST['hora']
        creditos = request.POST['creditos']
        estado = request.POST['estado']
        curso = Curso(
            codigo = codigo,
            nombre = nombre,
            hora = horas,
            creditos = creditos,
            estado = estado,
        )
        curso.save()
        return HttpResponse(f"Curso Creado: {curso.nombre} - {curso.codigo}")
    else:
        return HttpResponse("<h2> No se ha podido registrar el curso </h2>")

def listar_cursos(request):
    cursos = Curso.objects.all()
    """
    cursos = Curso.objects.filter(
        Q(nombre__contains="Py") |
        Q(nombre__contains="Hab")
    )
    """
    return render(request, 'listar_cursos.html',{
        'cursos': cursos,
        'titulo': 'Listado de Cursos'
    })

def eliminar_curso(request, id):
    curso = Curso.objects.get(pk=id)
    curso.delete()
    return redirect('listar_cursos')


