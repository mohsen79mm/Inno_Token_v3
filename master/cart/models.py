from django.db import models
from django.contrib.auth import get_user_model
from userprofile.models import cuser
# from restaurant.models import Food
from service.models import Service
User = get_user_model()


class Cart(models.Model):
    service = models.ManyToManyField(Service, through='CartItems')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"کاربر : {self.user.phone}"


class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    qty = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['cart', 'service'], name='cart item constraint')
        ]
    
    def __str__(self):
        return f'سرویس: {self.service} سبد خرید:{self.cart}'



class Factor(models.Model):  
    user = models.ForeignKey(cuser,on_delete=models.CASCADE)        
    total_price = models.PositiveIntegerField(default=0)
    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    update_time = models.TimeField(auto_now=True) 
    qty = models.PositiveIntegerField()
    

    def __str__(self):
        return f'کاربر : {self.user} | سرویس : {self.service}  | تعداد : {self.qty}  | مبلغ کل : {self.total_price}'





