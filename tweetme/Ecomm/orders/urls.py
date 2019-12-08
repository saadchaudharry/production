from django.urls import path
from .views import (OrderListView,OrderdetailView)

app_name="Order"
urlpatterns = [
    path('', OrderListView.as_view(), name='list'),
    path('<order_id>', OrderdetailView.as_view(), name='detail'),
]