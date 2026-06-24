from django.db import models
# Create your models here.


class Usuarios(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    password = models.CharField(max_length=64)

    class Meta:
        unique_together = ["name", "email"]
        ordering = ["name"]
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.name
