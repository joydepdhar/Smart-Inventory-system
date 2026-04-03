from django.db import transaction
from django.db.models import F
from inventory.models import Stock, StockMovement


class InventoryService:

    @staticmethod
    @transaction.atomic
    def stock_in(product, warehouse, quantity, user=None, reference_type="PURCHASE", reference_id=None):
        # Create movement
        StockMovement.objects.create(
            product=product,
            warehouse=warehouse,
            movement_type="IN",
            quantity=quantity,
            reference_type=reference_type,
            reference_id=reference_id,
            created_by=user
        )

        # Lock row for concurrency safety
        stock, _ = Stock.objects.select_for_update().get_or_create(
            product=product,
            warehouse=warehouse,
            defaults={'quantity': 0}
        )

        stock.quantity = F('quantity') + quantity
        stock.save()
        stock.refresh_from_db()

        return stock


    @staticmethod
    @transaction.atomic
    def stock_out(product, warehouse, quantity, user=None, reference_type="ORDER", reference_id=None):
        stock = Stock.objects.select_for_update().get(
            product=product,
            warehouse=warehouse
        )

        if stock.quantity < quantity:
            raise ValueError("Insufficient stock")

        # Create movement
        StockMovement.objects.create(
            product=product,
            warehouse=warehouse,
            movement_type="OUT",
            quantity=quantity,
            reference_type=reference_type,
            reference_id=reference_id,
            created_by=user
        )

        stock.quantity = F('quantity') - quantity
        stock.save()
        stock.refresh_from_db()

        return stock


    @staticmethod
    @transaction.atomic
    def transfer_stock(product, from_warehouse, to_warehouse, quantity, user=None):
        # OUT from source
        InventoryService.stock_out(
            product,
            from_warehouse,
            quantity,
            user,
            reference_type="ADJUSTMENT"
        )

        # IN to destination
        InventoryService.stock_in(
            product,
            to_warehouse,
            quantity,
            user,
            reference_type="ADJUSTMENT"
        )