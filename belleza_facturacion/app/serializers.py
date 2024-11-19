from rest_framework import serializers
from .models import Producto, Cliente, Factura, DetalleFactura

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class FacturaSerializer(serializers.ModelSerializer):
    detalles = serializers.StringRelatedField(many=True)

    class Meta:
        model = Factura
        fields = '__all__'
