from django.contrib import admin

# Register your models here.
from .models import  Coins, Rating

admin.site.register(Coins)
admin.site.register(Rating)
