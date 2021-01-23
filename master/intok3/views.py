from django.shortcuts import render 
from service import urls

def index(request):
        category = { 
        "startup_list":"استارتاپ",
        "provider_list":"خدمت دهنده",
        "accelerator_list":"مراکز معرفی",
        "services":"لیست سرویس ها ",
        "home":'خانه',
        "show_cart":'سبد خرید',
        "login":'ورود',
        "signup":'ثبت نام'
        }
        context = {
        'category':category
        }
        return render(request,'index.html',context)
