from django.db import models
from datetime import timezone

"""Criando as categorias"""
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

"""Criando os Autores"""
class Autor(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
    
class Livro(models.Model):
    titulo=models.CharField(max_length=200)
    autor=models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    publicado_em = models.DateField(default='')

    def __str__(self):
        return self.titulo
