from django.shortcuts import render, get_object_or_404
from userprofile.models import *
from .models import Subcategory, Category, Service
from django.views.generic import ListView,DetailView
from django.views import View

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


class userlist(View):
    def get(self,request,service_id):
        service_obj = get_object_or_404(Service, id=service_id)
        phone=service_obj.cuser
        # users = service_obj.use.all()
        user = cuser.objects.filter(phone__contains=phone)
        # print(users)
        # print(useraa)
        context = {
                'user':user
                }
        return render(request, 'user.html', context)


