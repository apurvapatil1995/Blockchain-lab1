from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import SaleItem, Txn

# Create your views here.

def index(request):
    item_list = SaleItem.objects.all()
    template = loader.get_template('webapp/index.html')
    context = {
            'item_list': item_list
        }
    return HttpResponse(template.render(context, request))

def sell(request):
    template = loader.get_template('webapp/sell.html')
    return HttpResponse(template.render(None, request))

def buy(request, item_id):
    item = SaleItem.objects.get(item_id=item_id)
    context = {
                'item': item
            }
    txn = Txn(buyer_id="admin", seller_id=item.seller_id, item=item_id)
    txn.save()
    item.set(available=False)
    template = loader.get_template('webapp/buy.html')
    return HttpResponse(template.render(context, request))
