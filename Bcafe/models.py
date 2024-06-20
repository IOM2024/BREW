from django.db import models

class Mycoffee(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='coffee_images/', blank=True, null=True)
    image_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def total_quantity(self):
        return sum(item.quantity for item in self.cartitem_set.all())

    class Meta:
        app_label = 'Bcafe'

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'Bcafe'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(Mycoffee, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    milk_quantity = models.PositiveIntegerField(default=0)
    sugar_quantity = models.PositiveIntegerField(default=0)
    water_quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.quantity} of {self.product.name}'

    class Meta:
        app_label = 'Bcafe'


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # Add additional fields as needed (e.g., customer info, status)

    def __str__(self):
        return f"Order {self.id} - {self.created_at}"
# Create your models here.
