from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.forms import IntegerField
from .models import cuser
from captcha.fields import CaptchaField
from service.models import Service,Category,Subcategory
class LoginForm(forms.Form):
    phone = forms.CharField(max_length=11, required=True)
    password = forms.CharField(widget=forms.PasswordInput)

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = cuser
        fields = ['user_type', 'last_name','phone', 'password1', 'password2']

class SmsPasswordForm(forms.Form):
    phone = forms.CharField(max_length=11, required=True)


class ChangePasswordForm(forms.Form):
    old_pass = forms.CharField(widget=forms.PasswordInput)
    new_pass = forms.CharField(widget=forms.PasswordInput)
    
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = cuser
        fields = ['phone', 'name_of_company']
class CaptchaTestForm(forms.Form):
        
    captcha = CaptchaField()



class Addservice(forms.ModelForm): 

    class Meta:
        model = Service
        fields = ['name', 'description','picture','price']
    