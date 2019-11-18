from django.db import models


# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=200, blank=False, null=False)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    desperdicio = models.DecimalField(max_digits=5, decimal_places=2)
    precio = models.IntegerField(blank=False, null=False)
    fechaVencimiento = models.DateField()

    def __str__(self):
        return self.nombre


class Plato(models.Model):
    nombre = models.CharField(max_length=200, blank=False, null=False)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    desperdicio = models.DecimalField(max_digits=5, decimal_places=2)
    precio = models.IntegerField(blank=False, null=False)
    listaProductos = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Inventario(models.Model):
    nombre = models.CharField(max_length=200, blank=False, null=False)
    precio = models.IntegerField(blank=False, null=False)
    listaProductos = models.ForeignKey(Producto, on_delete=models.CASCADE)

    #def machineLearning:


    def __str__(self):
        return self.nombre

class Restaurante(models.Model):
    nombre = models.CharField(max_length=200, blank=False, null=False)
    correo = models.EmailField(max_length=254, blank=False, null=False)
    direccion = models.CharField(max_length=200, blank=False, null=False)
    telefono = models.IntegerField(blank=False, null=False)
    contrasenia = models.CharField(max_length=50, blank=False, null=False)
    desperdicio = models.DecimalField(max_digits=5, decimal_places=2)
    promedioVisitantes = models.DecimalField(max_digits=5, decimal_places=2)
    listaPlatos = models.ForeignKey(Plato, on_delete=models.CASCADE)
    listaProductos = models.ForeignKey(Producto, on_delete=models.CASCADE)

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
