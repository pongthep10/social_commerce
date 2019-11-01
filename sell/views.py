from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Item

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

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
