# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from shopping.models import ShoppingList, ShoppingItem

# Register your models here.
from django.contrib import admin

class ShoppingListAdmin(admin.ModelAdmin):
    pass

class ShoppingItemAdmin(admin.ModelAdmin):

    pass



admin.site.register(ShoppingList, ShoppingListAdmin)
admin.site.register(ShoppingItem, ShoppingItemAdmin)