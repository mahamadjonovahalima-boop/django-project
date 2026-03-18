from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price=models.IntegerField()

    def __str__(self):
        return self.name

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart{self.id}"

class CartItem(models.Model):
    cart = models.ForeignKey('Cart',on_delete=models.CASCADE)
    product = models.ForeignKey('Product',on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product.name

class Order(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}"