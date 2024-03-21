from django.contrib import admin
from django.urls import path
from product.views import (product_list_api_view, product_detail_api_view, category_list_api_view,
                           category_detail_api_view, review_detail_api_view, review_list_api_view,
                           product_list_with_review_api_view)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products/', product_list_api_view),
    path('api/v1/products/<int:id>/', product_detail_api_view),
    path('api/v1/categories/', category_list_api_view),
    path('api/v1/categories/<int:id>/', category_detail_api_view),
    path('api/v1/reviews/', review_list_api_view),
    path('api/v1/reviews/<int:id>/', review_detail_api_view),
    path('api/v1/products/reviews/', product_list_with_review_api_view),
]
