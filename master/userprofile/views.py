from django.shortcuts import render, get_object_or_404, redirect
from .models import cuser
from django.views.generic import ListView,DetailView
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, CustomUserCreationForm


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


class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        form = LoginForm()
        context = {
            'form': form,
            'signup' : "ساخت اکانت"
        }
        return render(request, 'login.html', context)
    
    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            phone = request.POST['phone']
            password = request.POST['password']
            user = authenticate(request, phone=phone, password=password)

            if user:
                login(request, user)
                return redirect('/')
            else:
                return redirect('login')

class SignUp(View):
    def get(self, request):
        form = CustomUserCreationForm()
        context = {
            'form': form,
            'login' : 'لاگین'
        }

        return render(request, 'signup.html', context)

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

        context = {
            'form': form
        }
        return render(request, 'signup.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')




        
