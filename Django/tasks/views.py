from django.db.models import Max
from django.http import HttpResponse

from django.shortcuts import get_object_or_404, redirect, render
from .forms import ProjectForm, TaskForm
from .models import LigaEstadistica, Project, Task

def Home(request):
    contexto = {
        "titulo": "NOVACRONIX",
        "mensaje": "Administra por separado los jugadores y los clubs de fútbol.",
    }
    return render(request, "tasks/home.html", contexto)

def project_list(request):
    contexto = {
        "titulo": "EQUIPOS DE FUTBOL",
        "mensaje": "Organizacion de jugadores",
        "projects": Project.objects.order_by("-created_at"),
    }
    return render(request, "projects/projects.html", contexto)


def club_list(request):
    contexto = {
        "clubs": (
            LigaEstadistica.objects.values("club", "liga")
            .annotate(created_at=Max("created_at"))
            .order_by("club", "liga")
        ),
    }
    return render(request, "clubs/club_list.html", contexto)


def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect("tasks:home")
    else:
        form = TaskForm()

    return render(request, "tasks/task_form.html", {"form": form, "modo": "crear"})

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("tasks:home")
    else:
        form = TaskForm(instance=task)

    return render(request, "tasks/task_form.html", {"form": form, "modo": "editar"})

def register(request):
    """Registros de usuarios"""
    return HttpResponse("Registros de Usuarios en línea")

def presentacion(request):
    """Presentacion del programador"""
    return HttpResponse("Si logras ver esto tienes buen ojo")

def greeting(request, nombre):
    """Registro de usuarios"""
    return HttpResponse(
        f"Hola, {nombre}. Bienvenido a NOVACRONIX"
    )

def destination(request, titulo, nombre, cargo):
    """Registro de usuarios"""
    return HttpResponse(
        f"Bienvenido,{titulo} {nombre}, su cargo es {cargo}"
    )

def area_triangulo(request, base, altura):
    """Calcula el área de un triángulo"""
    return HttpResponse(f"El área del triángulo es: {(base * altura) / 2}")

def my_first_template(request):
    contexto = {
        "titulo": "EQUIPOS DE FUTBOL",
        "mensaje": "Organizacion de jugadores",
    }
    return render(request, "tasks/my-first-template.html", contexto)

def leads_like(request):
    contexto = {
        "titulo": "Programador",
        "nombre": "Dereck",
        "apellido": "Mera",
    }
    return render(request, "leads/leads-like.html", contexto)

def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            return redirect("tasks:projects")

    else:
        form = ProjectForm()

    return render(request, "projects/project_form.html", {"form": form, "modo": "crear"})

def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect("tasks:projects")
    else:
        form = ProjectForm(instance=project)

    return render(request, "projects/project_form.html", {"form": form, "modo": "editar"})

