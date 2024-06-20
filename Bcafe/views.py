from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from .models import Mycoffee, Cart, CartItem,Order

def add_to_cart(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Mycoffee, id=product_id)
        cart, created = Cart.objects.get_or_create(id=request.session.get('cart_id', None))
        request.session['cart_id'] = cart.id

        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += 1
        cart_item.save()

        return redirect('view_cart')

    return JsonResponse({'message': 'Invalid request'}, status=400)

def view_cart(request):
    cart = get_object_or_404(Cart, id=request.session.get('cart_id', None))
    cart_items = CartItem.objects.filter(cart=cart)
    context = {
        'cart': cart,
        'cart_items': cart_items
    }
    return render(request, 'shop/cart.html', context)

def update_cart_item(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(CartItem, id=item_id)
        item.quantity = request.POST.get('quantity', item.quantity)
        item.milk_quantity = request.POST.get('milk_quantity', item.milk_quantity)
        item.sugar_quantity = request.POST.get('sugar_quantity', item.sugar_quantity)
        item.water_quantity = request.POST.get('water_quantity', item.water_quantity)
        item.save()
        return redirect('view_cart')

def delete_cart_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('view_cart')

def product_list(request):
    products = Mycoffee.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def home(request):
    mycoffee_list = Mycoffee.objects.all()
    context = {'mycoffee_list': mycoffee_list}
    return render(request, 'shop/index.html', context) 
from django.shortcuts import render

def checkout(request):

    # Add any necessary logic for the checkout process here
    return render(request, 'shop/checkout.html')
def process_order(request):
    if request.method == 'POST':
        # Get the cart from the session or the database
        cart = Cart.objects.get(id=request.session['cart_id'])  # Example of retrieving cart
        
        # Create a new order
        order = Order.objects.create(cart=cart)
        
        # Clear the cart after processing the order
        cart.cartitem_set.all().delete()
    return redirect('order_confirmation')
    return redirect('checkout')

def order_confirmation(request):
    return render(request, 'shop/order_confirmation.html')
