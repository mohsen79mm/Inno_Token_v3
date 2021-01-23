from django.shortcuts import render, get_object_or_404, redirect, Http404
from .models import cuser , File
from django.views.generic import ListView,DetailView
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, CustomUserCreationForm, CaptchaTestForm, ChangePasswordForm, SmsPasswordForm ,Addservice ,CompleteProfileForm , StartupProfileForm, ProviderProfileForm, AcceleratorProfileForm, CompleteProfileForm, CaptchaTestForm, ChangePasswordForm, VerifyForm
from kavenegar import *
from sendsms import api
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission
from cart.models import Factor 
from service.models import Service
from django.core.files.storage import FileSystemStorage
from service.models import Category , Subcategory
from django.contrib.auth.mixins import LoginRequiredMixin


API_KEY = '4A7954397758375742704553337376623853334E6C446B61742B7947634D322B4A495A374A442F444A4B493D'

class StartupList(ListView):
    
     queryset = cuser.objects.filter(user_type="استارتاپ")
     template_name= 'startup_list.html'


class ProviderList(ListView):
    
     queryset = cuser.objects.filter(user_type="خدمت دهنده")
     template_name= 'provider_list.html'


class AcceleratorList(ListView):
    
     queryset = cuser.objects.filter(user_type="مرکز معرفی")
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
                return redirect('complete_profile')
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
            phone = request.POST['phone']
            password = request.POST['password1']
            user_type = request.POST['user_type']
            form.save()
            if user_type != 'کاربر':
                u = cuser.objects.get(phone=phone)
                permission = Permission.objects.get(name='Can added service')
                u.user_permissions.add(permission)
            
            
            user = authenticate(request, phone=phone, password=password)

            if user:
                login(request, user)
                return redirect('verify')

        context = {
            'form': form
        }
        return render(request, 'signup.html', context)

class Verify(View):
    code = cuser.objects.make_random_password(length=5, allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889") 
    print(code)

    def get(self, request):
        form = VerifyForm()
        print(request.user.phone)

        # api = KavenegarAPI('4A7954397758375742704553337376623853334E6C446B61742B7947634D322B4A495A374A442F444A4B493D')
        params = { 'sender' : '1000596446', 'receptor': request.user.phone, 'message' : Verify.code}
        print(Verify.code)
        # api.sms_send(params)

        context = {
            'form': form,
        }

        return render(request, 'verify.html', context)

    def post(self, request):
        form = VerifyForm(request.POST)
        input_code = request.POST['code']
        if form.is_valid() and input_code==Verify.code:
            logout(request)
            return redirect('login')

        else:
            return redirect('verify')

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
            # print(phone)
            user_obj = get_object_or_404(cuser, phone=phone)
            if user_obj:
                # print(user_obj.first_name)
                # print(user_obj.password)
                # api = KavenegarAPI('4A7954397758375742704553337376623853334E6C446B61742B7947634D322B4A495A374A442F444A4B493D')
                user_pass = cuser.objects.make_random_password(length=5, allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889") 
                print(user_pass)
                params = { 'sender' : '1000596446', 'receptor': phone, 'message' : user_pass}
                # print(user_obj.password)
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
        print(request.user.phone)
        context = {
            'form': form
        }
        return render(request, 'change_password.html', context)

    def post(self, request):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            old_pass = request.POST['old_pass']
            user = authenticate(request, phone=request.user.phone, password=old_pass)
            if user:
                new_pass = request.POST['new_pass']
                user.set_password(new_pass)
                user.save()
                return redirect('login')
            
            else:
                return HttpResponse("Old pass is not correct")
        return redirect('changepass')

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
    if user.user_type == 'کاربر' : 
        user_type = "کاربر"
    if user.user_type == 'استارتاپ' : 
        user_type = "استارتاپ"
    if user.user_type == 'خدمت دهنده' : 
        user_type = "خدمت دهنده"
    if user.user_type == 'مرکز معرفی' : 
        user_type = "مرکز معرفی"
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


class add_service(LoginRequiredMixin,View):
    login_url = 'login'

    def get(self, request):
        if request.user.has_perm('userprofile.can_add_service'):
            cats = Category.objects.all()
            form = Addservice()
            context = {
                'form': form,
                'cat':cats,
            }
            return render(request, 'add_service.html', context)
        return HttpResponse("you can not add service")

    def post(self, request):
        if request.user.has_perm('userprofile.can_add_service'):
            # request.POST.update({'cuser':request.user})
            form = Addservice(request.POST,request.FILES)
            # print(request.user)

            if form.is_valid():
                print('sub : ',request.POST.get('subs'))
                # tozih code = record service sakhte mishe bar in asas ke cuser = request.user  hamon shakshi ke 
                # dare to profile service ezafe mikone 
                # field picture ke to model service tarif shode bayad intory tarif beshe dast nazanid ke 
                # amper michasbonam XD  baghiasham moshakhase  XD  ba tashakor  haj mohsen
                Service.objects.create(cuser=request.user,name=request.POST.get('name'),
                description=request.POST.get('description'),price=request.POST.get('price'),subcategory=Subcategory.objects.get(id=request.POST.get('subs')),
                category=Category.objects.get(id=request.POST.get('category')),picture=FileSystemStorage().save(
                        f"{Service.picture.field.upload_to}/{request.FILES['picture'].name}", request.FILES['picture']))

                return redirect('user_profile') 
                
            else:
                return redirect('home')

def load_sub(request):
    programming_id = request.GET.get('programming')
    courses = Subcategory.objects.filter(category_id=programming_id).order_by('name')
    return render(request, 'subs.html', {'subs': courses})            

class CompleteProfile(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self, request):
        if request.user.user_type == "خدمت دهنده":
            form = ProviderProfileForm(instance=request.user)
        elif request.user.user_type == "استارتاپ":
            form = StartupProfileForm(instance=request.user)
        elif request.user.user_type == "مرکز معرفی":
            form = AcceleratorProfileForm(instance=request.user)
        else:
            form = CompleteProfileForm(instance=request.user)
        context = {
            'form': form,
        }
        return render(request, 'complete_profile.html', context)

    def post(self, request):
        if request.user.user_type == "خدمت دهنده":
            form = ProviderProfileForm(request.POST, request.FILES, instance=request.user)
            if form.is_valid() : 
                File.objects.create(user=request.user, file1=request.FILES['file1'], file2=request.FILES['file2'])
                form.save()

        elif request.user.user_type == "استارتاپ":
            form = StartupProfileForm(request.POST, request.FILES, instance=request.user)
            if form.is_valid() : 
                File.objects.create(user=request.user, file1=request.FILES['file1'])
                form.save()

        elif request.user.user_type == "مرکز معرفی":
            form = AcceleratorProfileForm(request.POST, request.FILES, instance=request.user)
            if form.is_valid(): 
                File.objects.create(user=request.user, file1=request.FILES['file1'], file2=request.FILES['file2'], file3=request.FILES['file3'])
                form.save()

        else:
            if form.is_valid(): 
                form.save()

        return redirect('/')

