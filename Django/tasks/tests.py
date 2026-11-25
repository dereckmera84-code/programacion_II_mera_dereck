from django.test import TestCase
from django.urls import reverse

from .models import LigaEstadistica, Project


class PlayerAndClubSectionsTests(TestCase):
    def test_home_links_to_separate_player_and_club_sections(self):
        response = self.client.get(reverse("tasks:home"))

        self.assertContains(response, reverse("tasks:projects"))
        self.assertContains(response, reverse("tasks:clubs"))

    def test_player_list_displays_age_and_description(self):
        Project.objects.create(name="Jugador de prueba", description="Delantero", edad=22)

        response = self.client.get(reverse("tasks:projects"))

        self.assertContains(response, "Jugador de prueba")
        self.assertContains(response, "Delantero")
        self.assertContains(response, "22")

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

    def test_removed_league_fields_are_not_in_model(self):
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
