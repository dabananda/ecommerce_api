from rest_framework.viewsets import ModelViewSet
from django.db.models import Count
from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(product_count=Count('products')).all()
    serializer_class = CategorySerializer
