from django.contrib import admin
from .models import *

class WishListAdmin(admin.ModelAdmin):
    list_display = ['item', 'user']

admin.site.register(WishList, WishListAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email']

admin.site.register(User, UserAdmin)
