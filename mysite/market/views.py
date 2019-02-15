from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView

def index(request):
    return HttpResponse("Hello, world. You're at the market index.")

class HomePageView (TemplateView):
	template_name = 'home.html'