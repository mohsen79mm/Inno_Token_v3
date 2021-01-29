from django.shortcuts import render , redirect
from service import urls

# def index(request):
#         category = { 
#         "startup_list":"استارتاپ",
#         "provider_list":"خدمت دهنده",
#         "accelerator_list":"مراکز معرفی",
#         "services":"لیست سرویس ها ",
#         "home":'خانه',
#         "show_cart":'سبد خرید',
#         "login":'ورود',
#         "signup":'ثبت نام'
#         }
#         if  request.user.is_authenticated:
#                 username=request.user.last_name
#         else:  
#                 username="AnonymousUser"
#         context = {
#         'category':category,
#         'username':username,
#         }
#         return render(request,'index.html',context)

def index(request) : 
    return redirect('https://moaliyari.ir/')