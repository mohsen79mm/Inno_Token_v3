from django.db import models
from service.models import Service
from userprofile.models import cuser

class Cart(models.Model):
    Service=models.ManyToManyField(Service)
    cuser=models.ForeignKey(cuser,on_delete=models.CASCADE)
    Quantity=models.IntegerField()
    is_final=models.BooleanField(default=False)