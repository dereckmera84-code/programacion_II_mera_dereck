from django.db import models


class Sensei(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Alumno(models.Model):
    sensei = models.ForeignKey(
        'Sensei',
        on_delete=models.CASCADE,
        related_name='alumnos')
    nombre = models.CharField(max_length=100)
    edad = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    misiones = models.ManyToManyField('Mision', related_name='alumnos', blank=True)

    def __str__(self):
        return self.nombre


class Perfil(models.Model):
    alumno = models.OneToOneField(Alumno, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='perfiles/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Perfil de {self.alumno}"


class Mision(models.Model):
    sensei = models.ForeignKey(
        'Sensei',
        on_delete=models.CASCADE,
        related_name='misiones')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


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


class LigaEstadistica(models.Model):
    club = models.CharField(max_length=100)
    liga = models.CharField(max_length=100, default="LigaPro")
    partidos_jugados = models.PositiveIntegerField()
    victorias = models.PositiveIntegerField()
    empates = models.PositiveIntegerField()
    derrotas = models.PositiveIntegerField()
    goles_a_favor = models.PositiveIntegerField()
    goles_en_contra = models.PositiveIntegerField()
    diferencia_goles = models.IntegerField()
    puntos_por_partido = models.DecimalField(max_digits=4, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["club", "liga"]

    def __str__(self):
        return f"{self.club} - {self.liga}"
