from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import SaleItem, Txn
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required
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
    template = loader.get_template('webapp/buy.html')
    item = SaleItem.objects.get(item_id=item_id)
    context = {
                'item': item
            }
    return HttpResponse(template.render(context, request))

def pay(request, item_id):
    template = loader.get_template('webapp/index.html')
    item = SaleItem.objects.get(item_id=item_id)
    context = {
                'item': item
            }
    txn = Txn(buyer_id=request.user, seller_id=item.seller_id, item_id=item)
    txn.save()
    item.available = False
    item.save()
    messages.add_message(request, messages.INFO, item.item_name + ' bought')
    item_list = SaleItem.objects.all()
    context = {
            'item_list': item_list
        }
    return HttpResponse(template.render(context, request))


