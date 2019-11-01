from django.db import models

class Item(models.Model):
    Name = models.CharField(max_length=200)
    Url = models.URLField(max_length=200)
    SellPrice = models.DecimalField( max_digits=5, decimal_places=2)
    Price = models.DecimalField( max_digits=5, decimal_places=2)
    Show = models.BooleanField(default=True)

class Order(models.Model):
    status = models.CharField(max_length=10, blank=True, null=True, default='PENDING') #PENDING, SUBMITTED
    created_at = models.DateField(auto_now_add=True)
    manychat_campaign = models.CharField(max_length=200, blank=True, null=True,)
    
class Orderitems(models.Model):
    OrderId = models.ForeignKey(Order, models.DO_NOTHING, blank=True, null=True)
    ItemId =  models.ForeignKey(Item, models.DO_NOTHING, blank=True, null=True)
    qty = models.IntegerField()

