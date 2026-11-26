from django import template

register = template.Library()

GRUPOS = [
    ("personas", "Personas", "Estudiantes y sus perfiles.", ["Estudiante", "Perfil"]),
    ("actividades", "Actividades", "Lo que se hace en el club y quién participa.",
     ["Actividad", "Mision", "Participacion"]),
    ("resultados", "Resultados", "Seguimiento del rendimiento en la liga.", ["LigaEstadistica"]),
    ("accesos", "Accesos", "Quién puede entrar y qué puede hacer.", ["User", "Group"]),
]

DESCRIPCIONES = {
    "Estudiante": "Quienes participan en las actividades.",
    "Perfil": "Foto e información de cada alumno.",
    "Actividad": "Entrenamientos, eventos y reuniones.",
    "Mision": "Retos y metas para los alumnos.",
    "Participacion": "Quién cumplió cada actividad y con qué rol.",
    "LigaEstadistica": "Puntajes y posiciones por temporada.",
    "User": "Cuentas con acceso a este panel.",
    "Group": "Permisos agrupados por función.",
}


@register.simple_tag
def agrupar_modelos(app_list):
    """Reparte los modelos del admin en las secciones del panel de inicio."""
    modelos = {m["object_name"]: m for app in app_list for m in app["models"]}
    grupos = []
    for id_grupo, titulo, detalle, nombres in GRUPOS:
        filas = [dict(modelos[n], desc=DESCRIPCIONES[n]) for n in nombres if n in modelos]
        if filas:
            grupos.append({"id": id_grupo, "titulo": titulo, "detalle": detalle, "filas": filas})
    return grupos
