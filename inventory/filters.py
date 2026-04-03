import django_filters
from inventory.models import StockMovement


class StockMovementFilter(django_filters.FilterSet):
    product = django_filters.NumberFilter(field_name='product_id')
    warehouse = django_filters.NumberFilter(field_name='warehouse_id')
    movement_type = django_filters.CharFilter(field_name='movement_type')

    class Meta:
        model = StockMovement
        fields = ['product', 'warehouse', 'movement_type']