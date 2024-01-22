from rest_framework import routers
from django.urls import path, include

from products.views import ProductViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls)),
    path('user/', UserViewSet.as_view()),
]