from django.urls import path
from .views import carts,cart_update,checkout_view,cart_delete,handlerequest,paytm

app_name="cart"

urlpatterns = [
    path('',carts,name='home'),
    path('update/',cart_update,name='update'),
    path('checkout/', checkout_view, name='checkout'),
    path('delete/', cart_delete, name='delete'),
    path("handlerequest/", handlerequest, name="handlerequest"),
    path('paytm',paytm,name="paytm")

]
