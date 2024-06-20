from django.urls import path
from .views import add_to_cart, product_list, home, view_cart, update_cart_item, delete_cart_item,checkout,process_order,order_confirmation

urlpatterns = [
    path('', home, name='home'),
    path('products/', product_list, name='product_list'),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),
    path('cart/update/<int:item_id>/', update_cart_item, name='update_cart_item'),
    path('cart/delete/<int:item_id>/', delete_cart_item, name='delete_cart_item'),
    path('checkout/', checkout, name='checkout'),
    path('process_order/', process_order, name='process_order'),
    path('order_confirmation/', order_confirmation, name='order_confirmation'),
]