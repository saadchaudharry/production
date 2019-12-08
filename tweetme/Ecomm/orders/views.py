from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from billing.models import Blilling
from django.http import Http404
from orders.models import Order

# Create your views here.

class OrderListView(LoginRequiredMixin,ListView):
    def get_queryset(self):
        return Order.objects.get_Billingprofile(self.request)

class OrderdetailView(LoginRequiredMixin,DetailView):
    template_name = "orders/order_detail.html"
    def get_queryset(self):
        return Order.objects.get_Billingprofile(self.request)

    def get_object(self, queryset=None):
        qs=Order.objects.get_Billingprofile(self.request).filter(order_id=self.kwargs.get('order_id'))
        if qs.count()==1:
            return qs.first
        else:
            raise Http404
