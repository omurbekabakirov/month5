from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product, Category, Review
from product.serializers import ProductSerializer, CategorySerializer, ReviewSerializer, Product2Serializer
from rest_framework import status


@api_view(['GET', 'POST'])
def product_list_api_view(request):
    product_list = Product.objects.all()
    data = ProductSerializer(product_list, many=True).data
    return Response(data=data)


@api_view(['GET'])
def product_list_with_review_api_view(request):
    if request.method == 'GET':
        product_list = Product.objects.all()
        data = Product2Serializer(product_list, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        product_serializer = CategorySerializer(data=request.data)
        product_serializer.is_valid(raise_exception=True)
        product_serializer.save()
        return Response(data=product_serializer, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, id):
    queryset = get_object_or_404(Product, id=id)
    if request.method == 'GET':
        serializer = ProductSerializer(queryset)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ProductSerializer(queryset)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def category_list_api_view(request):
    if request.method == 'GET':
        category_list = Category.objects.all()
        data = CategorySerializer(category_list, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        category_serializer = CategorySerializer(data=request.data)
        category_serializer.is_valid(raise_exception=True)
        category_serializer.save()
        return Response(data=category_serializer, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail_api_view(request, id):
    queryset = get_object_or_404(Category, id=id)
    if request.method == 'GET':
        serializer = CategorySerializer(queryset)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = CategorySerializer(queryset)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def review_list_api_view(request):
    review_list = Review.objects.all()
    data = ReviewSerializer(review_list, many=True).data
    return Response(data=data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    queryset = get_object_or_404(Review, id=id)
    if request.method == 'GET':
        serializer = ReviewSerializer(queryset)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(queryset)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

