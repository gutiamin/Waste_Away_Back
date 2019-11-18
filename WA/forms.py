from django import forms

from .models import *


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = '__all__'


class PlatoForm(forms.ModelForm):
    class Meta:
        model = Plato
        fields = '__all__'


class RestauranteForm(forms.ModelForm):
    class Meta:
        model = Restaurante
        fields = '__all__'


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'