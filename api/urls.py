from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('products/', views.product_list_api, name='product_list_api'),
    path('products/<int:pk>/', views.product_detail_api, name='product_detail_api'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]