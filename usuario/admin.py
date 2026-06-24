from django.contrib import admin

from usuario.models import Usuarios

# Register your models here.


@admin.register(Usuarios)
class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ("name", "password", "email")
