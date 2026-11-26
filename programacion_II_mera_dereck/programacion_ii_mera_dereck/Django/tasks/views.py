from django.db.models import Max
from django.shortcuts import render

from .models import LigaEstadistica


def home(request):
    contexto = {
        "titulo": "Clubs",
        "mensaje": "Consulta y administra tus clubs de fútbol.",
    }
    return render(request, "tasks/home.html", contexto)


def club_list(request):
    contexto = {
        "clubs": (
            LigaEstadistica.objects.values("club", "liga")
            .annotate(created_at=Max("created_at"))
            .order_by("club", "liga")
        ),
    }
    return render(request, "clubs/club_list.html", contexto)
