from django.contrib import admin
from core.models import Categoria, Autor, Livro

class Categorias(admin.ModelAdmin):
    list_display=('id','nome')
    list_display_links=('id','nome')
    search_fields=('nome',)
admin.site.register(Categoria, Categorias)

class Autores(admin.ModelAdmin):
    list_display=('id','nome')
    list_display_links=('id','nome')
    search_fields=('nome',)
admin.site.register(Autor,Autores)

class Livros(admin.ModelAdmin):
    list_display=('id','titulo','autor','categoria','publicado_em')
    list_display_links=('id','titulo')
    search_fields = ('titulo',)
admin.site.register(Livro,Livros)


