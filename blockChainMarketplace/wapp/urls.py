from django.urls import path

from . import views

app_name = 'blockChainMarketplace'

urlpatterns = [
    path('', views.index, name='index'),
    path('sell', views.sell, name='sell'),
    path('sellExec', views.sellExec, name='sellExec'),
    path('<int:item_id>/buy', views.buy, name='buy'),
    path('<int:item_id>/pay', views.pay, name='pay'),
]
