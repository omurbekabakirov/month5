from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product, Category, Review
from product.serializers import ProductSerializer, CategorySerializer, ReviewSerializer
from rest_framework import status


@api_view(['GET'])
def product_list_api_view(request):
    product_list = Product.objects.all()
    data = ProductSerializer(product_list, many=True).data
    return Response(data=data)


@api_view(['GET'])
def product_detail_api_view(request, id):
    try:
        product_detail = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error_message': 'Product does not exist'},
                        status=status.HTTP_404_NOT_FOUND)
    data = ProductSerializer(product_detail, many=False).data
    return Response(data=data)

@api_view(['GET'])
def category_list_api_view(request):
    category_list = Category.objects.all()
    data = CategorySerializer(category_list, many=True).data
    return Response(data=data)


@api_view(['GET'])
def category_detail_api_view(request, id):
    try:
        category_detail = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(data={'error_message': 'Category does not exist'},
                        status=status.HTTP_404_NOT_FOUND)
    data = CategorySerializer(category_detail, many=False).data
    return Response(data=data)


@api_view(['GET'])
def review_list_api_view(request):
    review_list = Review.objects.all()
    data = ReviewSerializer(review_list, many=True).data
    return Response(data=data)


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review_detail = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error_message': 'Review does not exist'},
                        status=status.HTTP_404_NOT_FOUND)
    data = ReviewSerializer(review_detail, many=False).data
    return Response(data=data)

