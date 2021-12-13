from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

app_name = 'pizzas'

urlpatterns = [
    path('', views.index, name='index'),
    path('Pizza', views.Pizza, name='pizza'),
    path('Pizzas/<int:pizza_id/', views.Pizza, name="Pizza"),
    
]
