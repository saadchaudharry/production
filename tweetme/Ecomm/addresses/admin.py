from django.contrib import admin
from .models import Address
# Register your models here.
class Addressadmin(admin.ModelAdmin):
    list_display = ['__str__','id']
    class Meta:
        model = Address
admin.site.register(Address,Addressadmin)
