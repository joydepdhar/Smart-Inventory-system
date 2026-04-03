from django.db import models
from django.core.validators import MinValueValidator
from products.models import Product
from warehouse.models import Warehouse
from django.conf import settings


# -------------------------------
# Stock (Current State)
# -------------------------------
class Stock(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='stocks'
    )
    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.CASCADE,
        related_name='stocks'
    )

    quantity = models.IntegerField(default=0)

    class Meta:
        db_table = 'stock'
        unique_together = ('product', 'warehouse')
        indexes = [
            models.Index(fields=['product', 'warehouse']),
        ]

    def __str__(self):
        return f"{self.product} - {self.warehouse} ({self.quantity})"


# -------------------------------
# Stock Movement (Source of Truth)
# -------------------------------
class StockMovement(models.Model):
    MOVEMENT_TYPE_CHOICES = [
        ('IN', 'Stock In'),
        ('OUT', 'Stock Out'),
        ('TRANSFER', 'Transfer'),
    ]

    REFERENCE_TYPE_CHOICES = [
        ('ORDER', 'Order'),
        ('PURCHASE', 'Purchase'),
        ('ADJUSTMENT', 'Adjustment'),
    ]

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='movements'
    )

    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.CASCADE,
        related_name='movements'
    )

    movement_type = models.CharField(max_length=10, choices=MOVEMENT_TYPE_CHOICES)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    reference_type = models.CharField(max_length=20, choices=REFERENCE_TYPE_CHOICES)
    reference_id = models.IntegerField(null=True, blank=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'stock_movements'
        indexes = [
            models.Index(fields=['product']),
            models.Index(fields=['warehouse']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f"{self.product} | {self.movement_type} | {self.quantity}"