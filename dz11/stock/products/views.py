from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.documents import ProductDocument, CategoryDocument, BrandDocument
from products.models import Product, Brand, Category
from products.serializers import ProductSerializer, BrandSerializer, CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@api_view(['GET'])
def search_products(request):
    query = request.query_params.get('name')
    if query is None:
        query = ' '
    products = ProductDocument.search().query("match", name=query)
    serializer = ProductSerializer(products.to_queryset(), many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def search_categories(request):
    query = request.query_params.get('name')
    if query is None:
        query = ' '
    products = CategoryDocument.search().query("match", name=query)
    serializer = CategorySerializer(products.to_queryset(), many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def search_brands(request):
    query = request.query_params.get('name')
    if query is None:
        query = ' '
    products = BrandDocument.search().query("match", name=query)
    serializer = BrandSerializer(products.to_queryset(), many=True, context={'request': request})
    return Response(serializer.data)



