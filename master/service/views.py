from django.shortcuts import render, get_object_or_404 , redirect
from userprofile.models import *
from .models import Subcategory, Category, Service
from django.views.generic import ListView,DetailView
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


class services(ListView):
    model = Service
    template_name = 'services_main.html'


class categorylist(ListView):
    model = Category
    template_name = 'categories.html'

#final changes

def subcategorylist(request , cat_id) : 

    sub = Subcategory.objects.filter(category__id=cat_id)

    if not sub : 
        print(HttpResponseRedirect(reverse('service_cat',kwargs={'cat_id' : cat_id })))
        return HttpResponseRedirect(reverse('service_cat',kwargs={'cat_id' : cat_id }))
    else : 
        context = {
            'object_list' : sub ,
        }
        return render(request, 'subcategories.html' , context)

        


class servicelist_sub(ListView):
    template_name = 'services.html'
    def get_queryset(self):
        return Service.objects.filter(subcategory__id=self.kwargs['sub_id'])


class servicelist_cat(ListView):
    template_name = 'services.html'
    def get_queryset(self):
        return Service.objects.filter(category__id=self.kwargs['cat_id'])


class service_detail(DetailView) : 
    model=Service
    template_name = 'service_detail.html'
    