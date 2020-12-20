from django.db import models
from django.contrib.auth import get_user_model

# from restaurant.models import Food
from service.models import Service
User = get_user_model()


class Cart(models.Model):
    service = models.ManyToManyField(Service, through='CartItems')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.email}"


class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    qty = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['cart', 'service'], name='cart item constraint')
        ]