from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from django.template import loader
from .models import Item, Order
from .forms import OrderForm


def index(request):
    return render(request, 'single_pdp/testform.html', {'form': OrderForm})

    # def get_name(request):
    #     # if this is a POST request we need to process the form data
    #     if request.method == 'POST':
    #         # create a form instance and populate it with data from the request:
    #         form = NameForm(request.POST)
    #         # check whether it's valid:
    #         if form.is_valid():
    #             # process the data in form.cleaned_data as required
    #             # ...
    #             # redirect to a new URL:
    #             return HttpResponseRedirect('/thanks/')
    #     # if a GET (or any other method) we'll create a blank form
    #     else:
    #         form = OrderForm()
    #     return render(request, 'single_pdp/testform.html', {'form': form})

def items(request):
    # if this is a POST request we need to process the form data

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        #  post = get_object_or_404(Order)

        if order_form.is_valid():
            new_order = order_form.save(commit=False)
            
            # username = order_form.cleaned_data['username']
            new_order.manychat_campaign = 'test'

            # Add item and request order here

            new_order.save()
            return redirect('thankyou')

    else:
        q = request.GET.getlist('p')
        manychatcampaign = request.GET.getlist('mnc')
        items = list(Item.objects.filter(NSQID__in=q))
        items.sort(key=lambda t: q.index(t.NSQID))

    return render(request, 'single_pdp/index.html',{ 'items': items,'form': OrderForm, 'cname': manychatcampaign})


def thankyou(request):
    return render(request, 'single_pdp/thank.html')
    
# def items(request):
#     q = request.GET.getlist('p')
#     items = list(Item.objects.filter(NSQID__in=q))
#     items.sort(key=lambda t: q.index(t.NSQID))

#     return render(request, 'single_pdp/index.html',{ 'items': items,'form': OrderForm})