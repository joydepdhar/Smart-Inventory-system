from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from inventory.models import Stock, StockMovement
from inventory.serializers import (
    StockSerializer,
    StockMovementSerializer,
    StockInSerializer,
    StockOutSerializer,
    TransferSerializer
)
from inventory.filters import StockMovementFilter

from products.models import Product
from warehouse.models import Warehouse

from services.inventory_service import InventoryService


# -------------------------------
# Stock View (Read Only)
# -------------------------------
class StockViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Stock.objects.select_related('product', 'warehouse')
    serializer_class = StockSerializer


# -------------------------------
# Stock Movement View (History)
# -------------------------------
class StockMovementViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StockMovement.objects.select_related('product', 'warehouse')
    serializer_class = StockMovementSerializer
    filterset_class = StockMovementFilter


# -------------------------------
# Stock IN API
# -------------------------------
class StockInView(APIView):
    def post(self, request):
        serializer = StockInSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product = get_object_or_404(Product, id=serializer.validated_data['product_id'])
        warehouse = get_object_or_404(Warehouse, id=serializer.validated_data['warehouse_id'])

        stock = InventoryService.stock_in(
            product=product,
            warehouse=warehouse,
            quantity=serializer.validated_data['quantity'],
            user=request.user
        )

        return Response({
            "message": "Stock added successfully",
            "current_quantity": stock.quantity
        }, status=status.HTTP_200_OK)


# -------------------------------
# Stock OUT API
# -------------------------------
class StockOutView(APIView):
    def post(self, request):
        serializer = StockOutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product = get_object_or_404(Product, id=serializer.validated_data['product_id'])
        warehouse = get_object_or_404(Warehouse, id=serializer.validated_data['warehouse_id'])

        try:
            stock = InventoryService.stock_out(
                product=product,
                warehouse=warehouse,
                quantity=serializer.validated_data['quantity'],
                user=request.user
            )
        except ValueError as e:
            return Response({"error": str(e)}, status=400)

        return Response({
            "message": "Stock deducted successfully",
            "current_quantity": stock.quantity
        })


# -------------------------------
# Transfer API
# -------------------------------
class TransferStockView(APIView):
    def post(self, request):
        serializer = TransferSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product = get_object_or_404(Product, id=serializer.validated_data['product_id'])
        from_warehouse = get_object_or_404(Warehouse, id=serializer.validated_data['from_warehouse_id'])
        to_warehouse = get_object_or_404(Warehouse, id=serializer.validated_data['to_warehouse_id'])

        InventoryService.transfer_stock(
            product=product,
            from_warehouse=from_warehouse,
            to_warehouse=to_warehouse,
            quantity=serializer.validated_data['quantity'],
            user=request.user
        )

        return Response({"message": "Stock transferred successfully"})