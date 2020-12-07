from django.shortcuts import render, get_object_or_404
from .models import Subcategory, Category, Service
from django.views.generic import ListView


class categorylist(ListView):
    model = Category
    template_name = 'categories.html'

class subcategorylist(ListView):
    # model = Subcategory
    template_name = 'subcategories.html'
    def get_queryset(self):
        return Subcategory.objects.filter(category__id=self.kwargs['cat_id'])




class servicelist(ListView):
    template_name = 'services.html'

    def get_queryset(self):

        return Service.objects.filter(subcategory__id=self.kwargs['sub_id'])


