from django import forms
from django.forms import ModelForm
from .models import Order,Orderitem


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'tel', 'address', 'district', 'amphoe', 'province', 'zipcode']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'textinputclass'}),
            'tel': forms.TextInput(attrs={'class': 'e   ditable medium-editor-textarea postcontent'}),
            'address': forms.TextInput(attrs={'class': 'e   ditable medium-editor-textarea postcontent'}),
            'district': forms.TextInput(attrs={'class': 'e   ditable medium-editor-textarea postcontent'}),
            'amphoe': forms.TextInput(attrs={'class': 'e   ditable medium-editor-textarea postcontent'}),
            'province': forms.TextInput(attrs={'class': 'e   ditable medium-editor-textarea postcontent'}),
            'zipcode': forms.TextInput(attrs={'class': 'e   ditable medium-editor-textarea postcontent'}),
        }

class ItemForm(ModelForm):
    class Meta:
        model = Orderitem
        fields = ['OrderId', 'ItemId', 'qty']




# class Address2(forms.Form):
#     name =forms.CharField(max_length=50) 
#     tel = forms.CharField(max_length=10, min_length=10, blank=False, null=False)
#     address = forms.CharField(max_length=70, blank=False, null=False)
#     district = forms.CharField(max_length=60, default="ตำบล", blank=False, null=False)
#     amphoe = forms.CharField(max_length=30, default="อำเภอ", blank=False, null=False)
#     province = forms.CharField(max_length=50)
#     zipcode = forms .CharField(max_length=5)

#     def __str__(self):
#         return self.name