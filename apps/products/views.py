from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from rest_framework.pagination import PageNumberPagination
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def test_json_view(request):
    data = {'name': 'John Doe', 'age': 30, 'location': 'New York', 'is_active': True}
    return JsonResponse(data)

@csrf_exempt
def test_post_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('user', 'Unknown')
        response_data = {'name': name, 'age': 30, 'location': 'New York', 'is_active': True}
        return JsonResponse(response_data)
    return JsonResponse({'error': 'POST method required'}, status=400)

class ProductList(APIView):
    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 3
        products = Product.objects.all()
        result_page = paginator.paginate_queryset(products, request)
        serializer = ProductSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

class MostExpensiveProduct(APIView):
    def get(self, request):
        product = Product.objects.order_by('-price').first()
        if product:
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        return Response({'error': 'No products found'}, status=404)

class ProductCreate(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductUpdate(APIView):
    def put(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=404)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
