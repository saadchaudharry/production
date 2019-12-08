from django.db import models
from billing.models import Blilling
# Create your models here.
Address_choices=(
    ("billing","Billing"),
    ("shipping","Shipping")
)

class Address(models.Model):
    bill        =models.ForeignKey(Blilling,on_delete=models.SET_NULL,null=True,blank=True)
    Address_type=models.CharField(max_length=120,choices=Address_choices)
    address_1   =models.CharField(max_length=120)
    address_2   =models.CharField(max_length=120,null=True,blank=True)
    country     =models.CharField(max_length=120,default="India")
    state       =models.CharField(max_length=120)
    city        =models.CharField(max_length=120)
    pin_code    =models.IntegerField()
    contact_no      =models.IntegerField(default=91)

    def __str__(self):
        return str(self.bill)
