from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.template import loader
from .models import Item
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
    q = request.GET.getlist('p')
    items = list(Item.objects.filter(NSQID__in=q))
    items.sort(key=lambda t: q.index(t.NSQID))
    template = loader.get_template('single_pdp/index.html')
    # print('ddddddddddddddddddddd',)
    context = {
        'items': items,
    }
    return HttpResponse(template.render(context, request))
