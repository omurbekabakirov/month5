
from django.urls import path
from users import views

urlpatterns = [
    path('api/v1/users/register/', views.register),
    path('api/v1/users/login/', views.login),
    path('api/v1/users/confirm/', views.confirm),
]