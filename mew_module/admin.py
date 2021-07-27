from django.contrib import admin
from .models import Product, Subscription
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock", "status", "image")

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("email",)

admin.site.register(Product, ProductAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
