import os

from pizzas.views import Pizzas

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizzeria.settings")

import django

django.setup()

from pizzas.models import Pizza, Toppings

toppings = Pizza.objects.all()

for topping in toppings:
    print(topping.id)
    print(topping.text)
    print(topping.date_added)
