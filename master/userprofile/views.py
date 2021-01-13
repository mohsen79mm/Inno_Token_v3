from django.shortcuts import render, get_object_or_404, redirect,Http404
from .models import cuser
from django.views.generic import ListView,DetailView
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, CustomUserCreationForm,CaptchaTestForm, ChangePasswordForm, SmsPasswordForm ,Addservice
from kavenegar import *
from sendsms import api
from .forms import SmsPasswordForm
from django.contrib.auth.decorators import login_required
from cart.models import Factor 
from service.models import Service
from django.core.files.storage import FileSystemStorage
from service.models import Category

API_KEY = '4A7954397758375742704553337376623853334E6C446B61742B7947634D322B4A495A374A442F444A4B493D'

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
        form2 = CaptchaTestForm(request.POST)
        context = {
            'form': form,
            'signup' : "ساخت اکانت",
            'form2':form2,
        }
        return render(request, 'login.html', context)
    
    def post(self, request):
        form = LoginForm(request.POST)
        form2 = CaptchaTestForm(request.POST)

        if form.is_valid()and form2.is_valid():
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

class SmsPassword(View):
    def get(self, request):
        form = SmsPasswordForm
        context = {
            'form': form
        }
        return render(request, 'sms_password.html', context)

    def post(self, request):
        form = SmsPasswordForm(request.POST)
        if form.is_valid():
            phone = request.POST['phone']
            print(phone)
            user_obj = get_object_or_404(cuser, phone=phone)
            if user_obj:
                print(user_obj.first_name)
                print(user_obj.password)
                # api = KavenegarAPI('4A7954397758375742704553337376623853334E6C446B61742B7947634D322B4A495A374A442F444A4B493D')
                user_pass = cuser.objects.make_random_password(length=5, allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889") 
                print(user_pass)
                params = { 'sender' : '1000596446', 'receptor': phone, 'message' : user_pass}
                print(user_obj.password)
                # api.sms_send(params)
                user_obj.set_password(user_pass)
                user_obj.save()
                context = {
                    'form': form
                }
                user = authenticate(request, phone=phone, password=user_pass)
                if user:
                    login(request, user)
                    return redirect('changepass')
                else:
                    return redirect('smspass')
            else:
                return HttpResponse("your phone is not login")

class ChangePassword(View):
    def get(self, request):
        form = ChangePasswordForm
        context = {
            'form': form
        }
        return render(request, 'change_password.html', context)
    #change password  is fucked up  old pass ba chi moghayese shode daghighan ? :|
    def post(self, request):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            print(request.user)
            old_pass = request.POST['old_pass']
            print(old_pass)
            new_pass = request.POST['new_pass']
            request.user.set_password(new_pass)
            request.user.save()

            return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def User_profile(request):
    user = request.user
    name = user.last_name
    phone=user.phone
    email = user.email
    address = user.address 
    fact = Factor.objects.filter(user=user).order_by('-date')
    if user.user_type == 'B' : 
        user_type = "کاربر"
    if user.user_type == 'S' : 
        user_type = "استارتاپ"
    if user.user_type == 'P' : 
        user_type = "خدمات دهنده"
    if user.user_type == 'A' : 
        user_type = "مراکز معرفی"
    context={
      'type' : user_type , 
      'user' : user , 
      'name' : name , 
      'phone' : phone , 
      'email' : email , 
      'address' : address ,
      'fact' : fact ,
    }
    return render(request,'User_profile.html',context)


class add_service(View):
    def get(self, request):
        form = Addservice()
        context = {
            'form': form,
            
        }

        return render(request, 'add_service.html', context)

    def post(self, request):
        # request.POST.update({'cuser':request.user})
        form = Addservice(request.POST,request.FILES)
        # print(request.user)

        if form.is_valid():
            # tozih code = record service sakhte mishe bar in asas ke cuser = request.user  hamon shakshi ke 
            # dare to profile service ezafe mikone 
            # field picture ke to model service tarif shode bayad intory tarif beshe dast nazanid ke 
            # amper michasbonam XD  baghiasham moshakhase  XD  ba tashakor  haj mohsen
            Service.objects.create(cuser=request.user,name=request.POST.get('name'),
            description=request.POST.get('description'),price=request.POST.get('price'),subcategory=None,
            category=Category.objects.get(id=request.POST.get('category'),),picture=FileSystemStorage().save(
                    f"{Service.picture.field.upload_to}/{request.FILES['picture'].name}", request.FILES['picture']))
            
            # print(instance)
            return redirect('user_profile') 
            
        else:
            return redirect('home')