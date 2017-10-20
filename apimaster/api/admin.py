from django.contrib import admin

from .models import Coinlist, Details

@admin.register(Coinlist)
class CoinAdmin(admin.ModelAdmin):
    list_display = ['name', 'nick', 'ammount', 'worth', 'roi', 'logo', 'price', 'weekcoins', 'active']

@admin.register(Details)
class Details(admin.ModelAdmin):
    list_display = ['data', 'nodesconf', 'bootstrap', 'nodecount', 'coinslocked', 'sharetime', 'mcap']
