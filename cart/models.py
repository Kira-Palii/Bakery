from django.db import models
from django.contrib.auth.models import User
from store.models import Product

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.product.title}"

    @property
    def total_price(self):
        return self.product.price * self.quantity

class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'Нове'),
        ('done', 'Виконано'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Користувач")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new', verbose_name="Статус")
    address = models.CharField(max_length=255, verbose_name="Адреса доставки", default='')

    def __str__(self):
        return f"Замовлення №{self.id}"

    @property
    def total_cost(self):
        return sum(item.cost for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product_title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def cost(self):
        return self.price * self.quantity