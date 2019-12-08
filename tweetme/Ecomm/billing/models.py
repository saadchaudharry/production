from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
import stripe
# Create your models here.
user =settings.AUTH_USER_MODEL

stripe.api_key='sk_test_opgUQ5bUIXuqxu1vYD3zOO2Q008cYv1db9'


class BillingProfileManager(models.Manager):
    def new_or_get(self, request):
        user = request.user
        guest_email_id = request.session.get('guest_email_id')
        created = False
        obj = None
        if user.is_authenticated:
            obj, created = self.model.objects.get_or_create(user=user, email=user.email)
        else:
            pass
        return obj,created

class Blilling(models.Model):
    user     =models.OneToOneField(user,on_delete=models.SET_NULL,unique=True,null=True)
    email    =models.EmailField()
    update   =models.DateTimeField(auto_now=True)
    timpstamp=models.DateTimeField(auto_now_add=True)
    active   =models.BooleanField(default=True)
    customer_id =models.CharField(max_length=120,null=True,blank=True)
    objects  =BillingProfileManager()

    def __str__(self):
        return str(self.email)
#
# def billing_paytm_stripe(sender,instance,*args,**kwargs):
#     if not instance.customer_id and instance.email:
#         print("stripe chacha maal aya hai")
#         customer =stripe.Customer.create(
#             email=instance.email)
#         instance.customer_id=customer
# post_save.connect(billing_paytm_stripe,sender=Blilling)

def user_created_rec(sender,instance,created,*args,**kwargs):
    if created and instance.email:
        Blilling.objects.get_or_create(user=instance, email=instance.email)

post_save.connect(user_created_rec,sender=user)