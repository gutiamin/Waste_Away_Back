from rest_framework import serializers
from . import models


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


class RestauranteSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = models.Restaurante


class InventarioSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = models.Inventario
