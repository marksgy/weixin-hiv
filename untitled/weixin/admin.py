from django.contrib import admin

# Register your models here.

from .models import OrderInfo, UserInfo


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'qq',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'qq','phone','methods',)


admin.site.register(OrderInfo, OrderAdmin)
admin.site.register(UserInfo, UserAdmin)