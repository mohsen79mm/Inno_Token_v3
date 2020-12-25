from django.shortcuts import render

def index(request):
    category = { 
        "startup_list":"استارتاپ",
        "provider_list":"خدمت دهنده",
        "accelerator_list":"مراکز معرفی",
    
    }

    context = {
        'category':category,
        'CANONICAL_PATH': request.build_absolute_uri(request.path),

     }
    return render(request,'index.html',context)

