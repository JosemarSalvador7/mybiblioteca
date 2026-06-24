from django.contrib import admin
from .models import Categoria, Emprestimo, Livros

admin.site.register(Livros)
admin.site.register(Emprestimo)
admin.site.register(Categoria)
