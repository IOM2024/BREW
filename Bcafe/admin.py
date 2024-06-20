from django.contrib import admin
from django.utils.html import format_html
from .models import Mycoffee, Cart, CartItem
from .forms import MycoffeeForm

class MycoffeeAdmin(admin.ModelAdmin):
    form = MycoffeeForm
    list_display = ('name', 'price', 'total_quantity', 'image_tag')

    def total_quantity(self, obj):
        return obj.total_quantity
    total_quantity.short_description = 'Total Quantity'

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 45px; height:45px;" />'.format(obj.image.url))
        elif obj.image_url:
            return format_html('<img src="{}" style="width: 45px; height:45px;" />'.format(obj.image_url))
        return "No Image"
    image_tag.short_description = 'Image'

admin.site.register(Mycoffee, MycoffeeAdmin)
admin.site.register(Cart)
admin.site.register(CartItem)
