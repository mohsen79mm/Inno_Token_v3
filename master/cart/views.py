from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed, Http404, HttpResponse
from django.db.models import Prefetch

from .models import Cart, CartItems,Factor
# from restaurant.models import Food
from service.models import Service

@login_required(login_url='login', redirect_field_name='next')
def show_cart(request):

    cart, status = Cart.objects.get_or_create(user=request.user)
    cart_item = CartItems.objects.filter(cart=cart)
    tprice = 0
    for e in cart_item : 
      tprice +=  e.service.price

    context = {
        'cart_item': cart_item , 
        'tprice' : tprice , 
    }

    return render(request, 'cart.html', context)


@login_required(login_url='login', redirect_field_name='next')
def add_cart(request, service_id):
    if request.method == "POST":
        cart, status = Cart.objects.get_or_create(user=request.user)

        cart_items = Cart.objects.prefetch_related(Prefetch(
            'service', queryset=CartItems.objects.select_related('service'))).get(user=request.user)

        try:
            cart_item = cart_items.service.get(service_id=service_id)
            cart_item.qty += 1
            cart_item.save()
        except:
            CartItems.objects.create(service_id=service_id, cart=cart, qty=1)

        return redirect(request.GET.get('next', 'show_cart'))
    return HttpResponseNotAllowed("shab bekheir ba anke gtfe budi sobh bekheir")


@login_required(login_url='login', redirect_field_name='next')
def delete_from_cart(request, service_id):
    
        # cart = request.cart
        cart_items = Cart.objects.prefetch_related(Prefetch(
            'service', queryset=CartItems.objects.select_related('service'))).get(user=request.user)

        try:
            cart_item = cart_items.service.get(service_id=service_id)
            cart_item.delete()
        except:
            return Http404()

        return redirect(request.GET.get('next', 'show_cart'))
    


@login_required(login_url='login', redirect_field_name='next')
def confirmation(request):
    if request.method == 'POST':
        
        query =CartItems.objects.filter(cart=Cart.objects.get(user=request.user))
        
        for item in query:
    
            Factor.objects.create(user=request.user,qty=item.qty,service=Service.objects.get(name=item.service.name),
            total_price=(item.service.price)*item.qty)
            item.delete()
    
        return redirect(request.GET.get('next', 'show_cart'))
    return HttpResponseNotAllowed("shab bekheir ba anke gtfe budi sobh bekheir")

