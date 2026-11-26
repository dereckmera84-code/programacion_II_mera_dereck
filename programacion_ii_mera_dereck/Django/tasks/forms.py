from django import forms
from django.contrib.auth.models import Group, Permission
from django.utils.text import capfirst

ACCIONES = [("view", "Ver"), ("add", "Agregar"), ("change", "Editar"), ("delete", "Eliminar")]
AREAS = [
    "estudiante", "perfil", "actividad", "mision",
    "participacion", "ligaestadistica", "user", "group",
]
ORDEN = {area: posicion for posicion, area in enumerate(AREAS)}


class MatrizPermisos(forms.CheckboxSelectMultiple):
    """Muestra los permisos como una tabla: una fila por área y una columna por acción."""

    template_name = "tasks/widgets/matriz_permisos.html"

    class Media:
        js = ["tasks/js/permisos.js"]

    def get_context(self, name, value, attrs):
        contexto = super().get_context(name, value, attrs)
        marcados = {str(v) for v in value or []}
        filas = {}
        for opcion, _etiqueta in self.choices:
            permiso = opcion.instance
            accion, _, area = permiso.codename.partition("_")
            plural = permiso.content_type.model_class()._meta.verbose_name_plural
            fila = filas.setdefault(area, {"nombre": capfirst(plural), "celdas": {}})
            fila["celdas"][accion] = {
                "id": opcion.value,
                "accion": accion,
                "marcado": str(opcion.value) in marcados,
                "etiqueta": f"{dict(ACCIONES)[accion]} {fila['nombre'].lower()}",
            }
        ordenadas = sorted(filas.items(), key=lambda par: ORDEN[par[0]])
        contexto["widget"]["acciones"] = [titulo for _, titulo in ACCIONES]
        contexto["widget"]["filas"] = [
            {"nombre": f["nombre"], "celdas": [f["celdas"].get(a) for a, _ in ACCIONES]}
            for _, f in ordenadas
        ]
        return contexto


class GrupoForm(forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.none(),
        required=False,
        widget=MatrizPermisos,
        label="Permisos",
        help_text="Marca lo que podrá hacer este grupo en cada área.",
    )

    class Meta:
        model = Group
        fields = ("name", "permissions")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        codenames = [f"{accion}_{area}" for accion, _ in ACCIONES for area in AREAS]
        self.fields["permissions"].queryset = Permission.objects.filter(
            codename__in=codenames,
            content_type__app_label__in=["tasks", "auth"],
        ).select_related("content_type")

    def clean_permissions(self):
        elegidos = set(self.cleaned_data["permissions"])
        if self.instance.pk:
            visibles = self.fields["permissions"].queryset
            elegidos |= set(self.instance.permissions.exclude(pk__in=visibles))
        return list(elegidos)
