from django.contrib import admin

from .models import Coinlist

@admin.register(Coinlist)
class CoinAdmin(admin.ModelAdmin):
    list_display = ['name', 'nick', 'ammount', 'worth', 'roi', 'logo', 'nodecount', 'coinslocked', 'sharetime', 'price', 'mcap', 'weekcoins', 'active']
