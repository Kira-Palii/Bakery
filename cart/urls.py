from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='cart_view'),
    path('add/<slug:slug>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.admin_order_list, name='admin_order_list'),
    path('orders/complete/<int:order_id>/', views.complete_order, name='complete_order'),
]