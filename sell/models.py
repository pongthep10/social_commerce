from django.db import models

class Items(models.Model):
    Name = models.CharField(max_length=200)
    SellPrice = models.DecimalField( max_digits=5, decimal_places=2)
    Price = models.DecimalField( max_digits=5, decimal_places=2)
    Show = models.BooleanField(default=True)

class Orders(models.Model):
    is_submitted = models.BooleanField(default=False)

class ItemsOrders(models.Model):
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)

