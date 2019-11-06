from django import forms
from django.forms import ModelForm
from .models import Order,Orderitem

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'tel', 'address', 'district', 'amphoe', 'province', 'zipcode', 'manychat_campaign']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'uk-input uk-width-1-1', 'name': 'namelastname',}),
            'tel': forms.TextInput(attrs={'class': 'uk-input uk-width-1-1', 'name': 'tel',}),
            'address': forms.TextInput(attrs={'class': 'uk-input uk-width-1-1', 'name': 'address',}),
            'district': forms.TextInput(attrs={'class': 'uk-input uk-width-1-1', 'name': 'district',}),
            'amphoe': forms.TextInput(attrs={'class': 'uk-input uk-width-1-1', 'name': 'amphoe',}),
            'province': forms.TextInput(attrs={'class': 'uk-input uk-width-1-1', 'name': 'province',}),
            'zipcode': forms.TextInput(attrs={'class': 'uk-input uk-width-1-1', 'name': 'zipcode',}),
            'manychat_campaign  ': forms.TextInput(attrs={'class': 'uk-input uk-width-1-1', 'name': 'manychat_campaign',})
        }
    
        #custom field
    product_list = forms.Textarea()

    #initialise custom field
    def __init__(self, user, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['product_list'] = forms.ModelChoiceField(queryset=Experience.objects.filter(user=user))

    #save custom field
    def save(self, commit=True):
        self.instance.about  = self.cleaned_data['product_list']
        super(OrderForm, self).save(commit=commit)

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