from django.db import models
from django.contrib.auth.models import AbstractUser
from .myusermanager import MyUserManager
from django.utils.translation import gettext_lazy as _
import os

def get_upload_path(instance,filename):
    return os.path.join(f"{instance.user_type}/{instance.username}",filename)
class cuser(AbstractUser) :
    
    phone = models.CharField(max_length=11, unique=True)

    REQUIRED_FIELDS = ['phone']
    objects = MyUserManager()

    CATEGORYNAME = [
        ("B", 'کاربر'),                          # B => Basic User
        ("S", 'استارتاپ'),                      # S => StartUp
        ("P", 'خدمات دهنده'),                  # P => Provider
        ("A", 'مرکز معرفی'),                  # A => Accelerator
    ]
    user_type = models.CharField(
         choices=CATEGORYNAME, max_length=1,default ='B')

    
    logo = models.ImageField(upload_to=get_upload_path, blank=True, null=True)
    email = models.EmailField(_('email address'),default ='')
    address = models.CharField(max_length=100 ,blank=True, null=True )
    website = models.CharField(max_length=30, blank=True, null=True)
    linkedin = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self) : 
        return self.username

