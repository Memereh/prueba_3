from tkinter import CASCADE
from django.db import models

# Create your models here.
class USUARIO(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=255)
    permisos = models.CharField(max_length=255,default="usuario")
    class Meta():
        db_table = 'usuario'
    def __str__(self):
        return self.nombre

