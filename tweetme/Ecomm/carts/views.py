from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from orders.models import Order
from billing.models import Blilling
from addresses.models import Address
from addresses.forms import Addressform
from .models import Cart
from products.models import Product
from paytm import Checksum
MERCHANT_KEY="SG4UY9spY6dyf!l6"
import stripe
stripe.api_key="sk_test_opgUQ5bUIXuqxu1vYD3zOO2Q008cYv1db9"
PUBLIC_KEY="pk_test_YzKPxdSZIFf7cPoKXWjHyANY00Af8tmViO"

# i.catagory+"/"+i.slug
def cart_api(request):
    cart_obj,new_obj=Cart.objects.new_or_get(request)
    products=[{'id':i.id,'title':i.title,'price':i.price,'url':i.get_absolute_url() }for i in cart_obj.products.all()]
    return JsonResponse({'products':products,'total':cart_obj.total,'subtotal':cart_obj.subtotal})

def carts(request):
    if request.user.is_authenticated:
        cart_obj,new_obj = Cart.objects.new_or_get(request)
        return render(request,'cart/cart.html',{'cart':cart_obj})
    else:
        return redirect('Login')

def cart_update(request):
    if request.user.is_authenticated:
        product_id=request.POST.get("product_id")
        prod_obj=Product.objects.get(id=product_id)
        cart_obj,new_obj = Cart.objects.new_or_get(request)
        if prod_obj in cart_obj.products.all():
            cart_obj.products.remove(prod_obj)
            added=False
        else:
            cart_obj.products.add(prod_obj)
            added=True
        request.session['cart_item']= cart_obj.products.count()
        if request.is_ajax():
            jsonData={
                "added":added,
                "removed":not added,
                "cartitem": cart_obj.products.count()
            }
            return JsonResponse(jsonData)
        return redirect("cart:home")
    else:
        return redirect('Login')

def checkout_view(request):
    order_obj = None
    billing_profile = None
    address_form=Addressform()
    shipping_address_id = request.session.get("shipping_address_id", None)

    # getting cart
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    if new_obj == cart_obj.products.count()==0:
        redirect("cart:home")
    # adding the billing profile
    user =request.user
    if user.is_authenticated:
        billing_profile,billilng_create = Blilling.objects.get_or_create(user=user, email=user.email)
    # getting order by cart and billing profile
    if billing_profile is not None:
        order_obj,order_obj_create=Order.objects.get_or_new(cart_obj,billing_profile)
        if shipping_address_id:
            order_obj.shipping_address = Address.objects.get(id=shipping_address_id)
            order_obj.state="c_delete"
            del request.session["shipping_address_id"]
            order_obj.save()
    context={
        "order_obj": order_obj,
        "billing_profile":billing_profile,
        "address_form":address_form,
    }

    return render(request,"cart/checkout.html",context)


def cart_delete(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    # deleting whole order by postsave signal
    billing_profile=None
    user = request.user
    if user.is_authenticated:
        billing_profile, billilng_create = Blilling.objects.get_or_create(user=user, email=user.email)
    order_obj, order_obj_create = Order.objects.get_or_new(cart_obj, billing_profile)
    order_obj.state = "o_delete"
    order_obj.save()
    return redirect("Products:p-all")


# testing paytm
def paytm(request):
    obj1 = request.POST.get('id')
    obj2 = request.POST.get('total')
    obj3 = request.POST.get('email')
    print(obj1,obj2,obj3)

    param_dict = {

        'MID': 'ZdehqP52015247605360',
        'ORDER_ID': str(obj1),
        'TXN_AMOUNT':str(obj2),
        'CUST_ID': str(obj3),
        'INDUSTRY_TYPE_ID': 'Retail',
        'WEBSITE': 'WEBSTAGING',
        'CHANNEL_ID': 'WEB',
        'CALLBACK_URL': 'http://127.0.0.1:8000/cart/handlerequest/',

    }
    param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
    return render(request, 'payment/paym.html', {'param_dict': param_dict})

@csrf_exempt
def handlerequest(request):
    form = request.POST
    checksum = None
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
    if checksum is not None:
        verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
        if verify:
            if response_dict['RESPCODE'] == '01':
                print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'payment/paymentstatus.html', {'response': response_dict})



