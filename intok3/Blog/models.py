from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
import os
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
def get_upload_path(instance,filename):
    return os.path.join(f"{instance.title}/{instance.author}",filename)


class post_category(models.Model) :
    category_name = models.CharField(max_length=50 , unique = True) 
    def __str__(self):
        return self.category_name


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    image=models.ImageField(upload_to=get_upload_path,null=True)
    content = RichTextField(blank = True , null = True)  
    post_cat = models.ManyToManyField(post_category )
    tag = TaggableManager()
    author = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)    
    updated_on = models.DateTimeField(auto_now= True)
    status = models.IntegerField(choices=STATUS, default=0)
    url = models.CharField(_("URL"), max_length=150, unique=True)    
    class Meta:
        ordering = ['-created_on']


    def __str__(self):
        return self.title
