from django.contrib import admin
from .models import Order

# Register your models here.
class Orderadmin(admin.ModelAdmin):
    search_fields = ["order_id"]
    list_display = ['__str__','billing_profile']
    class Meta:
        model = Order
admin.site.register(Order,Orderadmin)
