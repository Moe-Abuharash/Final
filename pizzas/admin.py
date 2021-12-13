from django.contrib import admin

# Register your models here.
from .models import Toppings, Pizza

admin.site.register(Pizza)
admin.site.register(Toppings)

