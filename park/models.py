from django.db import models

# Create your models here.
class UserTypeDiscount(models.Model):
    user_type=models.CharField(max_length=50)
    discount=models.DecimalField(max_digits=5, decimal_places=2)

class Ticket(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=50)
    age=models.PositiveIntegerField()
    user_type=models.CharField(max_length=50)
    price=models.DecimalField(decimal_places=2, max_digits=20, default=500)


