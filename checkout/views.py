
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KTPwkHVIV1508V7B1W0KazbwvKlLB7wm2HUt8Rj19Z94WHWgaX4bt30EfRY0k4RYeb4XjpAzQZ4zzx5H9jxqShI00tMAWvQmt'
        
    }

    return render(request, template, context)