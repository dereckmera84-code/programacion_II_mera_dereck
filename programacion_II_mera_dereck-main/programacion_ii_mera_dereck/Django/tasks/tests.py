from django.apps import apps
from django.contrib.auth.models import Group, Permission, User
from django.test import TestCase
from django.urls import reverse

from .models import LigaEstadistica


class ClubOnlyTests(TestCase):
    def test_home_displays_only_the_club_section(self):
        response = self.client.get(reverse("tasks:home"))

        self.assertContains(response, reverse("tasks:clubs"))
        self.assertNotContains(response, "Jugadores")

    def test_player_and_task_models_are_removed(self):
        model_names = {
            model.__name__ for model in apps.get_app_config("tasks").get_models()
        }

        self.assertTrue({"Project", "Task"}.isdisjoint(model_names))

    def test_club_list_displays_unique_club_and_league(self):
        club_data = {
            "club": "Club de prueba",
            "liga": "LigaPro",
            "partidos_jugados": 3,
            "victorias": 3,
            "empates": 0,
            "derrotas": 0,
            "goles_a_favor": 8,
            "goles_en_contra": 1,
            "diferencia_goles": 7,
            "puntos_por_partido": "3.00",
        }
        LigaEstadistica.objects.create(**club_data)
        LigaEstadistica.objects.create(**club_data)

        response = self.client.get(reverse("tasks:clubs"))

        self.assertContains(response, "Club de prueba")
        self.assertContains(response, "LigaPro")
        self.assertNotContains(response, "temporada")
        self.assertEqual(response.content.count(b"Club de prueba"), 1)

    def test_removed_club_fields_are_not_in_model(self):
        field_names = {field.name for field in LigaEstadistica._meta.get_fields()}

        self.assertTrue(
            {
                "temporada",
                "posicion",
                "puesto_grupo",
                "puntos",
                "porcentaje_victorias",
                "porcentaje_derrotas",
                "porcentaje_empates",
            }.isdisjoint(field_names)
        )


class PanelAdminTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.admin = User.objects.create_superuser("admin", password="clave-de-prueba")

    def setUp(self):
        self.client.force_login(self.admin)

    def test_inicio_agrupa_los_modelos_por_funcion(self):
        response = self.client.get(reverse("admin:index"))

        for texto in ("Personas", "Actividades", "Resultados", "Accesos", "Misiones"):
            self.assertContains(response, texto)
        self.assertContains(response, "Estadísticas de la liga")
        self.assertNotContains(response, "Senseis")

    def test_inicio_muestra_mensaje_si_no_hay_movimientos(self):
        response = self.client.get(reverse("admin:index"))

        self.assertContains(response, "Aún no hay movimientos")

    def test_formulario_de_grupo_muestra_la_tabla_de_permisos(self):
        response = self.client.get(reverse("admin:auth_group_add"))

        self.assertContains(response, "matriz-permisos")
        self.assertContains(response, "Solo lectura")
        self.assertContains(response, 'aria-label="Ver misiones"')

    def test_guardar_grupo_con_permisos_marcados(self):
        permiso = Permission.objects.get(codename="view_mision")

        self.client.post(
            reverse("admin:auth_group_add"),
            {"name": "Lectores", "permissions": [permiso.pk]},
        )

        grupo = Group.objects.get(name="Lectores")
        self.assertEqual(list(grupo.permissions.all()), [permiso])

    def test_editar_grupo_conserva_permisos_que_no_se_muestran(self):
        oculto = Permission.objects.get(codename="view_sensei")
        grupo = Group.objects.create(name="Antiguo")
        grupo.permissions.add(oculto)

        self.client.post(
            reverse("admin:auth_group_change", args=[grupo.pk]),
            {"name": "Antiguo", "permissions": []},
        )

        self.assertIn(oculto, grupo.permissions.all())
