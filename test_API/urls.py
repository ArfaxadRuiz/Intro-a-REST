from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet
from .views_profile import ProfileView  # Importar correctamente

router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')

urlpatterns = [
    path('', include(router.urls)),
    path('perfil/', ProfileView.as_view(), name='perfil'),
]
