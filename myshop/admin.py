from django.contrib import admin
from .models import Product, Purchase, Return
from myshop.models import MyUser
from django.contrib.auth.admin import UserAdmin

admin.site.register(MyUser, UserAdmin)
admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(Return)

