from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.http import is_safe_url

import stripe
# Create your views here.
stripe.api_key="sk_test_opgUQ5bUIXuqxu1vYD3zOO2Q008cYv1db9"
PUBLIC_KEY="pk_test_YzKPxdSZIFf7cPoKXWjHyANY00Af8tmViO"

def payment_method(request):
    next_url = None
    next_ = request.GET.get('next')
    if is_safe_url(next_, request.get_host()):
        next_url = next_
    return render(request,'payment/payment.html',{'publish_key':PUBLIC_KEY, "next_url": next_url})

@csrf_exempt
def payment_method_create(request):
    if request.method =='POST' and request.is_ajax():
        return JsonResponse({'message':'success!your card was added'})
    return HttpResponse('nikel auswe')