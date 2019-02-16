from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
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

def sellExec(request):
    sell = SaleItem(seller_id=request.user, item_name=request.POST['item_name'], item_desc=request.POST['item_desc'], price=request.POST['price'])
    sell.save()
    item_list = SaleItem.objects.all()
    template = loader.get_template('webapp/index.html')
    context = {
            'item_list': item_list
        }
    return HttpResponse(template.render(context, request))

def buy(request, item_id):
    item = SaleItem.objects.get(item_id=item_id)
    context = {
                'item': item
            }
    txn = Txn(buyer_id=request.user, seller_id=item.seller_id, item_id=item)
    txn.save()
    item.available = False
    item.save()
    item_list = SaleItem.objects.all()
    template = loader.get_template('webapp/buy.html')
    return HttpResponse(template.render(context, request))


