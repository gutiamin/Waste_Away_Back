from django.db import models

# Create your models here.

class Restaurante(models.Model):
    nombre = models.CharField(max_length=200, blank=False, null=False)
    correo = models.EmailField(max_length=254, blank=False, null=False)
    direccion = models.CharField(max_length=200, blank=False, null=False)
    telefono = models.IntegerField(blank=False, null=False)
    contrasenia = models.CharField(max_length=50, blank=False, null=False)
    desperdicio = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
	return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200, blank=False, null=False)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    desperdicio = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.nombre

class Plato(models.Model):
    nombre = models.CharField(max_length=200, blank=False, null=False)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    desperdicio = models.DecimalField(max_digits=5, decimal_places=2)
    precio = models.IntegerField(blank=False, null=False)
    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=200, blank=False, null=False)
    correo = models.EmailField(max_length=254, blank=False, null=False)
    id = models.CharField(max_length=200, blank=False, null=False, primary_key=True)
    contrasenia = models.CharField(max_length=50, blank=False, null=False)
    desperdicio = models.DecimalField(max_digits=5, decimal_places=2)
    edad = models.IntegerField()
    estatura = models.IntegerField()
    peso = models.IntegerField()
    genero = models.CharField(max_length=15, blank=False, null=False)
    condicion_medica = models.CharField(max_length=150, blank=False, null=False)
    alergias = models.CharField(max_length=150, blank=False, null=False)
    def __str__(self):
        return self.nombre


