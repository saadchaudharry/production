from django.db import models
from django.conf import settings
from products.models import Product
from django.db.models.signals import pre_save,post_save,m2m_changed
from django.contrib.auth.models import User
# Create your models here.

user =User

class Cartmanger(models.Manager):
    def new_or_get(self,request):
        cart_id = request.session.get("cart_id",None)
        obj2 = self.get_queryset().filter(user=request.user)
        if (obj2.exists() == True):
            cart_obj=obj2.first()
            new_obj = False
        else:
            cart_obj = Cart.objects.create(user=request.user)
            print('ye hua ')
            request.session["cart_id"]=cart_obj.id
            new_obj = True
        return cart_obj,new_obj

    # def new_cart(self,user=None):
    #     print(user)
    #     user_obj=None
    #     if user is not None:
    #         if user.is_authenticated:
    #             user_obj=user
    #     return self.model.objects.create(user=user_obj)


class Cart(models.Model):
    user      =models.OneToOneField(user,on_delete=models.SET_NULL,null=True,blank=True,unique=True)
    products  =models.ManyToManyField(Product,blank=True)
    subtotal  =models.DecimalField(default=0.00,max_digits=1000,decimal_places=2)
    total     =models.DecimalField(default=0.00,max_digits=1000,decimal_places=2)
    update    =models.DateTimeField(auto_now=True)
    timestamp =models.DateTimeField(auto_now_add=True)

    objects   =Cartmanger()

    def __str__(self):
        return str(self.id)

def subtotal_save(sender,instance,action,*args,**kwargs):
    if action=="post_add" or action=="post_remove" or action=="post_clear":
        product = instance.products.all()
        total = 0
        for i in product:
            total += i.price
        instance.subtotal = total
        instance.save()
m2m_changed.connect(subtotal_save,sender=Cart.products.through)


def total_save(sender,instance,*args,**kwargs):
    if instance.subtotal >0:
        instance.total =instance.subtotal + 100
    else:
        instance.total=0.00

pre_save.connect(total_save,sender=Cart)

def user_created_cart(sender,instance,created,*args,**kwargs):
    if created and instance:
        Cart.objects.get_or_create(user=instance)

post_save.connect(user_created_cart,sender=user)