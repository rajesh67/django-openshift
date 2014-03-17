from django.db import models
from django.contrib.auth.models import User
from .strings import *
# Create your models here.
from datetime import datetime

class Merchant(models.Model):
	name=models.CharField(max_length=30)
	url=models.URLField(max_length=30)
	affiliate_id=models.CharField(max_length=30)
	total_orders=models.PositiveIntegerField(default=0)
	

class Order(models.Model):
	ORDER_STATUS=(
		('E','EXPIRED'),
		('N','NEW'),
		('R','REJECTED'),
		('A','APPROVED'),
		('P','PENDING')
	)
	user=models.ForeignKey(User)
	number=models.PositiveIntegerField(default=0)
	merchant=models.ForeignKey(Merchant)
	created_on=models.DateTimeField(default=datetime.now())
	item_link=models.URLField(max_length=300)
	track_link=models.URLField(max_length=400,verbose_name=TRACK_LINK)
	status=models.CharField(choices=ORDER_STATUS,max_length=10,default='N')
	ammount=models.FloatField(default=0.00)
	rate=models.FloatField(default=0.00)
	cashback=models.FloatField(default=0.00)
	
	verification=models.BooleanField(default=False)



class UserProfile(User):
	orders=models.ManyToManyField(Order)
	#------bank details--------
	payee=models.CharField(max_length=30)
	bank_name=models.CharField(max_length=30)
	bank_account=models.CharField(null=True,max_length=30)
	bank_ifsc=models.CharField(max_length=15)
	tax_id=models.CharField(max_length=10)


