from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inventory.views import (
    StockViewSet,
    StockMovementViewSet,
    StockInView,
    StockOutView,
    TransferStockView
)

router = DefaultRouter()
router.register(r'stock', StockViewSet)
router.register(r'movements', StockMovementViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('stock-in/', StockInView.as_view()),
    path('stock-out/', StockOutView.as_view()),
    path('transfer/', TransferStockView.as_view()),
]