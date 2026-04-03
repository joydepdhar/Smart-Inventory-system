from rest_framework import serializers
from inventory.models import Stock, StockMovement
from products.models import Product
from warehouse.models import Warehouse


# -------------------------------
# Stock Serializer
# -------------------------------
class StockSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    warehouse_name = serializers.CharField(source='warehouse.name', read_only=True)

    class Meta:
        model = Stock
        fields = [
            'id',
            'product',
            'product_name',
            'warehouse',
            'warehouse_name',
            'quantity'
        ]


# -------------------------------
# Stock Movement Serializer
# -------------------------------
class StockMovementSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    warehouse_name = serializers.CharField(source='warehouse.name', read_only=True)

    class Meta:
        model = StockMovement
        fields = '__all__'


# -------------------------------
# Action Serializers (IMPORTANT)
# -------------------------------
class StockInSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    warehouse_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)


class StockOutSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    warehouse_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)


class TransferSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    from_warehouse_id = serializers.IntegerField()
    to_warehouse_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)