from django.contrib import admin

from .models import Project, Task


admin.site.site_header = "NOVACRONIX | Administración"
admin.site.site_title = "Administración NOVACRONIX"
admin.site.index_title = "Gestión de jugadores y tareas"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "edad", "description", "created_at")
    search_fields = ("name", "description")
    ordering = ("name",)
    list_per_page = 25


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "project", "status", "due_date")
    list_filter = ("status", "project")
    search_fields = ("title", "description", "project__name")
    list_select_related = ("project",)
    ordering = ("due_date", "title")
    list_per_page = 25

from django.contrib import admin

from .models import LigaEstadistica


@admin.register(LigaEstadistica)
class LigaEstadisticaAdmin(admin.ModelAdmin):
    list_display = (
        "club",
        "partidos_jugados",
        "victorias",
        "empates",
        "derrotas",
    )
    list_filter = ("liga",)
    search_fields = ("club",)