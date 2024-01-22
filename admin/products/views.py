from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from products.models import Product, User
from products.serializers import ProductSerializer, UserSerializer
from products.producer import publish



class ProductViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_created', serializer.data)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_updated', serializer.data)
        return Response(serializer.data)
    
    def destroy(self, request, pk=None):
        product = Product.objects.get(pk=pk)
        product.delete()
        publish('product_deleted', pk)
        return Response('Product deleted successfully!')
    

class UserViewSet(APIView):

    def get(self, request):
        queryset = User.objects.order_by('?').first()
        serializer = UserSerializer(queryset)
        return Response(serializer.data)
