from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class SaleItem(models.Model):
    item_id = models.AutoField(primary_key=True)
    seller_id = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length = 25)
    item_desc = models.CharField(max_length = 200)
    price = models.IntegerField()
    available = models.BooleanField(default=True)

class Txn(models.Model):
    seller_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="seller")
    buyer_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="buyer")
    item_id = models.ForeignKey(SaleItem, on_delete=models.DO_NOTHING)
