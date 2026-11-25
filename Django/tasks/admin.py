from django.contrib import admin

from .models import LigaEstadistica


admin.site.site_header = "NOVACRONIX | Administración"
admin.site.site_title = "Administración NOVACRONIX"
admin.site.index_title = "Gestión de clubs"


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