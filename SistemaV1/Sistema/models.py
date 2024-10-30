from django.db import models

class Usuario(models.Model):
    id = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    username = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    senha = models.CharField(
        default=255,
        null=False,
        blank=False
    )
    objetos = models.Manager()

# Create your models here.
