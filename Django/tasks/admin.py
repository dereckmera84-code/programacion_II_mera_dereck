from django.contrib import admin

# Register your models here.
from .models import Project, NominaTrabajo, Task


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "project", "status", "due_date")
    list_filter = ("status", "project")
    search_fields = ("title", "description")

@admin.register(NominaTrabajo)
class NominaTrabajoAdmin(admin.ModelAdmin):
    list_display = ("nombre_trabajador", "anio_contrato", "sueldo_asignado", "created_at")
    search_fields = ("nombre_trabajador",)
from django.contrib import admin

from .models import LigaEstadistica


@admin.register(LigaEstadistica)
class LigaEstadisticaAdmin(admin.ModelAdmin):
    list_display = (
        "club",
        "temporada",
        "posicion",
        "puntos",
        "partidos_jugados",
        "victorias",
        "empates",
        "derrotas",
    )
    list_filter = ("liga", "temporada")
    search_fields = ("club",)