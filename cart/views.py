from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from store.models import Product
from .models import CartItem, Order, OrderItem

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.total_price for item in cart_items)
    
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('cart_view')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    return redirect('cart_view')

@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    
    if not cart_items.exists():
        return redirect('products')

    if request.method == 'POST':
        address = request.POST.get('address')

        order = Order.objects.create(user=request.user, address=address)

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product_title=item.product.title,
                price=item.product.price,
                quantity=item.quantity
            )

        cart_items.delete()
        
        return redirect('products')
        
    return redirect('cart_view')

@login_required
def admin_order_list(request):
    if not request.user.is_superuser:
        return redirect('products')

    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'cart/admin_orders.html', {'orders': orders})

@login_required
def complete_order(request, order_id):
    if not request.user.is_superuser:
        return redirect('products')
        
    order = get_object_or_404(Order, id=order_id)

    order.delete()

    return redirect('admin_order_list')