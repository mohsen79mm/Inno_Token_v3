from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jmodels
from ckeditor.fields import RichTextField
import os

def get_upload_path(instance,filename):
    return os.path.join(f"{instance.user.user_type}/{instance.user.phone}",filename)

def get_upload_logo_path(instance,filename):
    return os.path.join(f"{instance.user_type}/{instance.phone}",filename)


class CustomUserManager(BaseUserManager):
    def create_user(self, phone, password, **extra_fields):
    
        if not phone:
            raise ValueError(_('The Phone must be set'))
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password, **extra_fields):
    
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(phone, password, **extra_fields)


class cuser(AbstractUser) :
    username = None
    phone = models.CharField(max_length=11, unique=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


    CATEGORYNAME = [
        ("کاربر", "کاربر"),                         
        ("استارتاپ", "استارتاپ"),                     
        ("خدمت دهنده", "خدمت دهنده"),                  
        ("مرکز معرفی", "مرکز معرفی"),                 
    ]
    user_type = models.CharField(
         choices=CATEGORYNAME, max_length=11,default ="کاربر")

    name_of_company = models.CharField(max_length=100 ,blank=True, null=True )
    logo = models.ImageField(upload_to=get_upload_logo_path, blank=True, null=True ,default=None)
    email = models.EmailField(_('email address'),default ='')
    address = models.CharField(max_length=100 ,blank=True, null=True )
    website = models.CharField(max_length=30, blank=True, null=True)
    linkedin = models.CharField(max_length=20, blank=True, null=True)
    content = RichTextField(blank = True, null=True)
    date_joined = jmodels.jDateTimeField(auto_now_add=True)

    def __str__(self) : 
        return self.last_name

    class Meta:
        permissions = (
            ('can_add_service', 'Can added service'),
        )

class File(models.Model):
    user = models.ForeignKey(cuser, related_name='file', on_delete=models.RESTRICT)
    file1 = models.FileField(upload_to=get_upload_path, blank=True, null=True) 
    file2 = models.FileField(upload_to=get_upload_path, blank=True, null=True) 
    file3 = models.FileField(upload_to=get_upload_path, blank=True, null=True) 
    file4 = models.FileField(upload_to=get_upload_path, blank=True, null=True) 
    file5 = models.FileField(upload_to=get_upload_path, blank=True, null=True) 


    def __str__(self) : 
        return self.user.last_name
