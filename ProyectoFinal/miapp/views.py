from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

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

