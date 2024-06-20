from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg

@register.filter
def cart_total(cart_items):
    total = 0
    for item in cart_items:
        total += item.product.price * item.quantity
    return total

