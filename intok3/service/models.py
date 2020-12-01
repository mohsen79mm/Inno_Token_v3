from django.db import models
from userprofile.models import cuser
from intok3 import settings


class Category(models.Model): 

    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 250)
    picture = models.ImageField(upload_to='logo/', blank=True,null=True)

    def __str__(self) :
        return self.name


class Subcategory(models.Model): 

    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 250)
    picture = models.ImageField(upload_to='logo/', blank = True , null = True)
    category = models.ForeignKey(Category , on_delete = models.CASCADE ,related_name='cat')

    def __str__(self) :
        return self.name



class Service(models.Model) : 

    name = models.CharField(max_length = 30)
    subcategory = models.ForeignKey(Subcategory , on_delete = models.CASCADE , blank = True , null = True,related_name='subcategory')
    category = models.ForeignKey(Category , on_delete = models.CASCADE,related_name='category')
    cuser = models.ForeignKey(cuser,related_name='use',on_delete=models.CASCADE)
    description = models.CharField(max_length = 250)
    picture = models.ImageField(upload_to='logo/', blank = True , null = True)
    price = models.IntegerField()
    
    def __str__(self) :
        return self.name


