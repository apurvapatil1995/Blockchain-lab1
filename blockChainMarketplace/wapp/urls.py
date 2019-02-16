from django.urls import path

from . import views

app_name = 'blockChainMarketplace'

urlpatterns = [
    path('', views.index, name='index'),
    path('sell', views.sell, name='sell'),
    path('<int:item_id>/buy', views.buy, name='buy'),
]
