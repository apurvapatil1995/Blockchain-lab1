from django.db import models

# Create your models here.
class username(models.Model) :
	username_text = models.CharField(max_length = 200)

class email(models.Model):
	email_text = models.CharField(max_length = 200)
