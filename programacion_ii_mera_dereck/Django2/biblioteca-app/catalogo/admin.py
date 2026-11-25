from django.contrib import admin

from .models import Autor, Categoria, Libro


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'nacionalidad')
    search_fields = ('nombre', 'apellido')


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'isbn', 'fecha_publicacion')
    list_filter = ('categoria',)
    search_fields = ('titulo', 'isbn')
