from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import SaleItem

# Create your views here.

def index(request):
    item_list = SaleItem.objects.all()
    template = loader.get_template('webapp/index.html')
    context = {
            'item_list': item_list
        }
    return HttpResponse(template.render(context, request))
