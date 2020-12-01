from django.shortcuts import render, get_object_or_404
from .models import Subcategory, Category, Service
from userprofile.models import *

def show_categories(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,

    }
    return render(request, 'categories.html', context)


def show_sub(request, cat_id):
    cat_obj = get_object_or_404(Category, id=cat_id)
    subs = cat_obj.cat.all()
    context = {
        'subcategory': subs,
    }
    return render(request, 'subcategories.html', context)


def show_service(request, subcategory_id):
    subcategory_obj = get_object_or_404(Subcategory, id=subcategory_id)

    services = subcategory_obj.subcategory.all()

    context = {

        'service': services,

    }
    return render(request, 'services.html', context)

def show_user_service(request,service_id):
    service_obj = get_object_or_404(Service,id=service_id)
    # print(service_obj.cuser)
    # print('------------------------------')
    user_query = cuser.objects.all().filter(username__startswith=str(service_obj.cuser))
    # print(ob_1)
    # users = Service.objects.all().select_related("cuser")
    # print(users)
    # users=service_obj.select_related("use").all()
    context = {
        'user':user_query,
    }


    return render(request,'service_provider.html',context)