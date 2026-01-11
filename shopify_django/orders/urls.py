from django.urls import path
from .views import shopify_order_webhook, order_list, order_detail

urlpatterns = [
     path('api/shopify/webhook/order/', shopify_order_webhook),
     path('orders/', order_list, name='order_list'),
     path('orders/<str:order_id>/', order_detail, name='order_detail'),
]