from .models import Service
def footer (request):
    
    Services=Service.objects.all().order_by('id')[:4]
    print(Services)
    return  {'FServices':Services}