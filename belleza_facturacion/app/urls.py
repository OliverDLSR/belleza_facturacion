
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import ProductoViewSet, ClienteViewSet, FacturaViewSet

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'facturas', FacturaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
