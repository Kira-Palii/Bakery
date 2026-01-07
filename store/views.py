from django.shortcuts import render
from .models import Product, Category

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', {'products': products})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'store/categories.html', {'categories': categories})