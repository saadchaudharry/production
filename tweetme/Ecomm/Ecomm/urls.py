"""Ecomm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import LogoutView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from django.urls import path,include
from .views import home,contact,regester,loog
from accounts.views import Login
from carts.views import cart_api
from addresses.views import checkout_address
from billing.views import payment_method,payment_method_create
from products.views import (Productfeaturedlistview
                            ,Productfeaturedslug,
                            Productcat,
                            Productfish,
                            Productdog,
                            Productaccessories,
                            Productbird,
                            #cata slug
                            Productcatslug,
                            Productbirdslug,
                            Productdogslug,
                            Productfishslug,
                            Productaccessoriesslug)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('contact/',contact,name='contact'),
    # account
    path('regester/',regester,name='regester'),
    path('loog/',loog,name='loog'),
    path('LogoutView/',LogoutView.as_view(template_name='auth/logout.html'),name='LogoutView'),
    path('PasswordReset/',PasswordResetView.as_view(template_name='auth/password_reset.html'),name='password_reset'),
    path('PasswordReset/<uidb64>/<token>',PasswordResetConfirmView.as_view(template_name='auth/password_reset_confirm.html'),name='password_reset_confirm'),
    path('PasswordReset/done',PasswordResetDoneView.as_view(template_name='auth/password_reset_done.html'),name='password_reset_done'),
    path('login/', Login,name='Login'),
    # search
    path('search/', include('search.urls', namespace="search")),
    path('billing/payment',payment_method,name='payment_method'),
    path('billing/payment/create/', payment_method_create, name='billing-payment-method-endpoint'),

    # product
    path('products/', include('products.urls', namespace="Products")),
    path('cart/', include('carts.urls', namespace="cart")),
    path('checkout_address/', checkout_address,name='checkout_add'),
    path('api/cart/', cart_api,name='cart_api'),
    # order
    path('order/', include('orders.urls', namespace="order")),

    #featured
    path('featured/', Productfeaturedlistview.as_view(),name='featured'),
    path('featured/<slug:slug>/', Productfeaturedslug.as_view(),name='featured_slug'),
    # cats
    path('cats/', Productcat.as_view(), name='cat'),
    path('cats/<slug:slug>/', Productcatslug.as_view(), name='cat_slug'),
    # fish
    path('fish/', Productfish.as_view(), name='fish'),
    path('fish/<slug:slug>/', Productfishslug.as_view(), name='fish_slug'),
    # dog
    path('dogs/', Productdog.as_view(), name='dog'),
    path('dogs/<slug:slug>/', Productdogslug.as_view(), name='dog_slug'),
    #bird
    path('birds/', Productbird.as_view(), name='bird'),
    path('birds/<slug:slug>/', Productbirdslug.as_view(), name='bird_slug'),
    #accessories
    path('accessories/', Productaccessories.as_view(), name='accessories'),
    path('accessories/<slug:slug>/', Productaccessoriesslug.as_view(), name='accessories_slug'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns +static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)