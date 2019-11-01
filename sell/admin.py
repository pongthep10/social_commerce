from django.contrib import admin
from .models import Orderitem, Order, Item

admin.site.register(Orderitem)
admin.site.register(Order)
admin.site.register(Item)