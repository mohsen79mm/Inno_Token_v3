from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import cuser
from captcha.fields import CaptchaField
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