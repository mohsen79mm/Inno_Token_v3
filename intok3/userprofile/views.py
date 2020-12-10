from django.shortcuts import render, get_object_or_404
from .models import cuser
from django.views.generic import ListView,DetailView



class StartupList(ListView):
    
     queryset = cuser.objects.filter(user_type="S")
     template_name= 'startup_list.html'


class ProviderList(ListView):
    
     queryset = cuser.objects.filter(user_type="P")
     template_name= 'provider_list.html'


class AcceleratorList(ListView):
    
     queryset = cuser.objects.filter(user_type="A")
     template_name= 'accelerator_list.html'         
    
class StartupDetail(DetailView):
     model=cuser
     template_name= 'startup_detail.html' 

class ProviderDetail(DetailView):
     model=cuser
     template_name= 'provider_detail.html' 

class AcceleratorDetail(DetailView):
     model=cuser
     template_name= 'accelerator_detail.html' 