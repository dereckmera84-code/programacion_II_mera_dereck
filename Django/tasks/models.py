from django.db import models

class NominaTrabajo(models.Model):
    nombre_trabajador = models.CharField(max_length=100)
    anio_contrato = models.IntegerField()
    sueldo_asignado = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_trabajador

class Sensei(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.TextField(blank=True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    sensei = models.ForeignKey(
            'Sensei', 
            on_delete=models.CASCADE,
            related_name='alumnos')
    nombre = models.CharField(max_length=100)
    edad = models.TextField(blank=True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    misiones = models.ManyToManyField('Mision', related_name='alumnos', blank=True)

    def __str__(self):
        return self.nombre

class Perfil(models.Model):
    alumno = models.OneToOneField(Alumno, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='perfiles/')
    created_at = models.DateTimeField(auto_now_add=True)

class Mision(models.Model):
    sensei = models.ForeignKey(
            'Sensei',
            on_delete=models.CASCADE,
            related_name='misiones')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank = True)
    created_at = models.DateTimeField(auto_now_add=True)


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    titulo = models.CharField(max_length=100)
    objetivo = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    estudiante = models.ManyToManyField(Estudiante,
                    through='Participacion')

class Participacion(models.Model):
    estudiante = models.ForeignKey(
        Estudiante,
        on_delete=models.CASCADE
    )
    actividad = models.ForeignKey(
        Actividad,
        on_delete=models.CASCADE
    )
    rol = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    class Status(models.TextChoices):
        TODO = "TODO", "Por hacer"
        IN_PROGRESS = "IN_PROGRESS", "En progreso"
        DONE = "DONE", "Completada"

    # ForeignKey: cada Task pertenece a UN Project.
    # Un Project puede tener MUCHAS Task — relación muchos a uno.
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tasks",
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.TODO,
    )
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class LigaEstadistica(models.Model):
    club = models.CharField(max_length=100)
    liga = models.CharField(max_length=100, default="LigaPro")
    temporada = models.CharField(max_length=20, blank=True)
    posicion = models.PositiveSmallIntegerField(blank=True, null=True)
    puesto_grupo = models.CharField(max_length=100, blank=True)
    puntos = models.PositiveIntegerField()
    partidos_jugados = models.PositiveIntegerField()
    victorias = models.PositiveIntegerField()
    empates = models.PositiveIntegerField()
    derrotas = models.PositiveIntegerField()
    goles_a_favor = models.PositiveIntegerField()
    goles_en_contra = models.PositiveIntegerField()
    diferencia_goles = models.IntegerField()
    porcentaje_victorias = models.DecimalField(max_digits=5, decimal_places=2)
    porcentaje_empates = models.DecimalField(max_digits=5, decimal_places=2)
    porcentaje_derrotas = models.DecimalField(max_digits=5, decimal_places=2)
    goles_anotados_por_partido = models.DecimalField(max_digits=4, decimal_places=2)
    goles_recibidos_por_partido = models.DecimalField(max_digits=4, decimal_places=2)
    puntos_por_partido = models.DecimalField(max_digits=4, decimal_places=2)
    ultimos_resultados = models.CharField(
        max_length=20,
        help_text="Secuencia usando G, E y P",
    )
    fuente = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-temporada", "posicion", "club"]
        constraints = [
            models.UniqueConstraint(
                fields=["club", "liga", "temporada"],
                name="unique_liga_estadistica_club_liga_temporada",
            )
        ]

    def __str__(self):
        return f"{self.club} - {self.temporada or self.liga}"