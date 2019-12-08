from django.urls import path
from products.views import (Productlistview,
                            Productdetailview,
                            Productslugdetailview,
                            #catagory
                            Productfeaturedlistview,
                            Productbird,
                            Productcat,
                            Productaccessories,
                            Productdog,
                            Productfish)

app_name="Products"
urlpatterns = [
    #for product
    path('',Productlistview.as_view(), name='p-all'),#products/
    path('<int:pk>/',Productdetailview.as_view(), name='detail'),#products/1/
    path('<slug:slug>/',Productslugdetailview.as_view(), name='slug'),#products/name/
    #catagory

]

# path('products/featured/', Productfeaturedlistview.as_view(), name='featured'),  # products/featured/
# path('products/bird/', Productbird.as_view(), name='bird'),  # products/featured/
# path('products/cat/', Productcat.as_view(), name='cat'),  # products/featured/
# path('products/accessories/', Productaccessories.as_view(), name='accessories'),  # products/featured/
# path('products/dog/', Productdog.as_view(), name='dog'),  # products/featured/
# path('products/fish/', Productfish.as_view(), name='fish'),  # products/featured/