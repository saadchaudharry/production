from django.shortcuts import render,redirect
from .forms import Addressform
from django.utils.http import is_safe_url
from billing.models import Blilling
# Create your views here.

def checkout_address(request):
    form =Addressform(request.POST or None)
    context={
        "form":form,
    }
    next_=request.GET.get('next')
    next_post=request.POST.get('next')
    redirect_path= next_ or next_post or None
    if form.is_valid():
        instance = form.save(commit=False)
        user=request.user
        billing_profile,billilng_create = Blilling.objects.get_or_create(user=user, email=user.email)
        if billing_profile is not None:
            address_type=request.POST.get('Address_type',"shipping")
            instance.bill=billing_profile
            instance.Address_type=address_type
            instance.save()
            request.session['shipping_address_id'] = instance.id
        else:
            print('error')
            return redirect(redirect_path)

        if is_safe_url(redirect_path,request.get_host()):
            redirect(redirect_path)
        else:
            return redirect("cart:checkout")
    return redirect("cart:checkout")