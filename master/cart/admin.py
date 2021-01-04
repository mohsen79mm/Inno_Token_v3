from django.contrib import admin

from .models import Cart, CartItems,Factor


class CartItemInline(admin.TabularInline):
    model = CartItems


class CartAdmin(admin.ModelAdmin):
    inlines = [
        CartItemInline,
    ]


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItems)
admin.site.register(Factor)