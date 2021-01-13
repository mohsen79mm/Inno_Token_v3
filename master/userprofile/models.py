from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jmodels
import os

def get_upload_path(instance,filename):
    return os.path.join(f"{instance.user_type}/{instance.username}",filename)

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
        ("B", 'کاربر'),                          # B => Basic User
        ("S", 'استارتاپ'),                      # S => StartUp
        ("P", 'خدمات دهنده'),                  # P => Provider
        ("A", 'مرکز معرفی'),                  # A => Accelerator
    ]
    user_type = models.CharField(
         choices=CATEGORYNAME, max_length=1,default ='B')

    name_of_company = models.CharField(max_length=100 ,blank=True, null=True )
    logo = models.ImageField(upload_to=get_upload_path, blank=True, null=True ,default=None)
    email = models.EmailField(_('email address'),default ='')
    address = models.CharField(max_length=100 ,blank=True, null=True )
    website = models.CharField(max_length=30, blank=True, null=True)
    linkedin = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    date_joined = jmodels.jDateTimeField(auto_now_add=True)

    def __str__(self) : 
        return self.last_name

