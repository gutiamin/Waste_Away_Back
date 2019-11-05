from rest_framework import serializers
from . import models


class RestauranteSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = models.Restaurante


class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = models.Producto

class PlatoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = models.Plato

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = models.Cliente
