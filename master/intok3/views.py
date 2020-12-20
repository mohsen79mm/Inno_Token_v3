from django.shortcuts import render

def index(request):
    category = { 
        "startup_list":"استارتاپ",
        "provider_list":"خدمت دهنده",
        "accelerator_list":"مراکز معرفی"
    }

    context = {
        'category':category
     }
    return render(request,'index.html',context)
    