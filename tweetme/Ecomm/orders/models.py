from django.db import models
from products.models import Product
from carts.models import Cart
from addresses.models import Address
from billing.models import Blilling
from django.db.models.signals import pre_save,post_save
from Ecomm.utils import unique_order_id_genrator
import datetime

ORDER_STATUS_CHOICES=(
    ('created','Created'),
    ('paid','Paid'),
    ('shipped','Shipped'),
    ('refunded','Refunded'),
    ('delivered','Delivered'),
    ('cancel','Cancel')
)
ORDER_STATE_CHOICES=(
    ("c_delete","c_delete"),
    ("o_delete","o_delete")
)


# Create your models here.
class Ordermodelqueryset(models.query.QuerySet):
    def get_Billingprofile(self,request):
        user_profile,created=Blilling.objects.new_or_get(request)
        return self.filter(billing_profile=user_profile)


class Ordermanager(models.Manager):
    def get_queryset(self):
        return Ordermodelqueryset(self.model,using=self._db)

    def get_Billingprofile(self,request):
        return self.get_queryset().get_Billingprofile(request)

    def get_or_new(self,cart_obj,billing_profile):
        order_qs = self.get_queryset().filter(cart=cart_obj, billing_profile=billing_profile)
        if order_qs.count() == 1:
            order_obj = order_qs.first()
            created=True
        else:
            order_obj = self.get_queryset().create(cart=cart_obj, billing_profile=billing_profile)
            created=False
        return order_obj,created

class Order(models.Model):
    order_id        =models.CharField(max_length=120,blank=True)
    cart            =models.ForeignKey(Cart,on_delete=models.SET_NULL,null=True,blank=True)
    shipping_address=models.ForeignKey(Address,on_delete=models.SET_NULL,null=True,blank=True)
    billing_profile =models.ForeignKey(Blilling,on_delete=models.SET_NULL,null=True,blank=True)
    status          =models.CharField(max_length=120,choices=ORDER_STATUS_CHOICES,default='created')
    state           =models.CharField(max_length=120,choices=ORDER_STATE_CHOICES,default=None,null=True,blank=True)
    total           =models.DecimalField(default=0.00,max_digits=1000,decimal_places=2)
    prods           =models.ManyToManyField(Product,blank=True)
    order_date      =models.DateField(default=datetime.date.today)
    active          =models.BooleanField(default=True)
    objects =Ordermanager()

    def __str__(self):
        return str(self.order_id)

    def update_total(self):
        cart_total=self.cart.total
        cart_prod=self.cart.products.all()
        self.prods.set(cart_prod)
        self.total=cart_total
        self.save()
        return cart_total


def pre_save_order_id_genrator(sender,instance,*args,**kwargs):
    if not instance.order_id:
        instance.order_id=unique_order_id_genrator(instance)
    qs =Order.objects.filter(cart=instance.cart).exclude(billing_profile=instance.billing_profile)
    if qs.exists():
        qs.update(active=False)

pre_save.connect(pre_save_order_id_genrator,sender=Order)


def post_save_cart_total(sender,instance,created,*args,**kwargs):
    if not created:
        cart_obj=instance
        cart_id=cart_obj.id
        cart_prod=cart_obj.products
        qs =Order.objects.filter(cart__id=cart_id)
        if qs.count()==1:
            order_obj=qs.first
            order_obj.update_total()

post_save.connect(post_save_cart_total,sender=Cart)

def post_save_order(sender,instance,created,*args,**kwargs):
    if created:
        instance.update_total()

post_save.connect(post_save_order,sender=Order)

def post_save_cart(sender,instance,created,*args,**kwargs):
    if instance.state=='c_delete':
        instance.cart.delete()

post_save.connect(post_save_cart,sender=Order)

def cancel_signal(sender,instance,created,*args,**kwargs):
    if instance.state=='o_delete':
        cart_obj=instance.cart
        cart_id=cart_obj.id
        obj=Order.objects.filter(cart__id=cart_id)
        obj.delete()
post_save.connect(cancel_signal,sender=Order)


