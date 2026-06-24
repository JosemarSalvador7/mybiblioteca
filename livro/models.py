import datetime
from django.db import models  # type: ignore
from datetime import date
from usuario.models import Usuarios


class Categoria(models.Model):
    name = models.CharField(max_length=50)
    descricao = models.TextField()
    usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ["name"]
        unique_together = ["name", "descricao", "usuario"]

    def __str__(self):
        return self.name


class Livros(models.Model):
    img =  models.ImageField(upload_to='capa_livro' ,blank=False,null=False,)
    titulo = models.CharField(max_length=100, blank=False)
    autor = models.CharField(max_length=50, blank=False)
    co_autor = models.CharField(max_length=50, blank=True)
    data_cadastro = models.DateField(default=date.today())
    emprestado = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"
        ordering = ["titulo"]
        unique_together = ["titulo", "autor", "co_autor"]

    def __str__(self):
        return self.titulo



class Emprestimo(models.Model):
    choices = (
        ("P", "Péssimo"),
        ("R", "Ruim"),
        ("B", "Bom"),
        ("O", "Otimo"),
    )
    nome_emprestado = models.ForeignKey(
        Usuarios, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    nome_emprestado_anonimo = models.CharField(max_length=50, blank=True)
    data_emprestimo = models.DateTimeField(default=datetime.datetime.now())
    data_devolucao = models.DateTimeField(blank=True, null=True)
    livro = models.ForeignKey(Livros, on_delete=models.DO_NOTHING)
    avaliacao = models.CharField(max_length=1, choices=choices, null=True, blank=True)

    def __str__(self):
        return f"{self.nome_emprestado} | {self.livro}"
