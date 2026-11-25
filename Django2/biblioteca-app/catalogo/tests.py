from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from catalogo.form.libro_form import LibroForm
from catalogo.models import Autor, Categoria, Libro


class LibroTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin',
        )
        self.client.force_login(self.user)
        self.categoria = Categoria.objects.create(nombre='Novela')
        self.autor = Autor.objects.create(
            nombre='Gabriel',
            apellido='García Márquez',
        )

    def test_libro_form_includes_autores(self):
        form = LibroForm()

        self.assertIn('autores', form.fields)

    def test_libro_can_be_searched_by_author(self):
        libro = Libro.objects.create(
            titulo='Cien años de soledad',
            fecha_publicacion=timezone.localdate(),
            categoria=self.categoria,
            isbn='9780307474728',
        )
        libro.autores.add(self.autor)

        response = self.client.get(
            reverse('libro_list'),
            {'pista': 'Gabriel'},
        )

        self.assertContains(response, 'Cien años de soledad')


class AutorUpdateTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin',
        )
        self.client.force_login(self.user)
        self.autor = Autor.objects.create(
            nombre='Mario',
            apellido='Benedetti',
        )

    def test_autor_update_uses_existing_model_and_form(self):
        response = self.client.post(
            reverse('autor_update', args=[self.autor.pk]),
            {
                'nombre': 'Mario',
                'apellido': 'Benedetti',
                'nacionalidad': 'Uruguaya',
            },
        )

        self.autor.refresh_from_db()
        self.assertRedirects(response, reverse('autor_list'))
        self.assertEqual(self.autor.nacionalidad, 'Uruguaya')
