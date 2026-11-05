from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class LugarPatrimonial(models.Model):
    nombre = models.CharField(max_length=150)
    description = models.TextField()
    ubicacion = models.CharField(max_length=200)
    anio_construccion = models.IntegerField()
    imagen = models.URLField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='lugares')


    def __str__(self):
        return self.nombre
