from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pizzas/index.html')



def Pizza(request):
    toppings = Pizza.objects.order_by('date_added')

    context = {'Pizza': Pizza}

    return render(request, "pizzas/Pizza.html", context)


def Pizzas(request):
    pizzas = Pizza.objects.get()
    toppings = pizzas.entry_set.all()

    context = {'Pizza': Pizza, 'toppings':'toppings'} 
    return render(request, "pizzas/toppings.html", context)
