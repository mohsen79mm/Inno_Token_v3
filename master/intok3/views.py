from django.shortcuts import render

def index(request):
    category = { 

        "show_cart":"سبد خرید",
        
        "startup_list":"استارتاپ",
        "provider_list":"خدمت دهنده",
        "accelerator_list":"مراکز معرفی",
        "category-list":"سرویسها"
    }

    context = {
        'category':category
     }
    return render(request,'index.html',context)
    