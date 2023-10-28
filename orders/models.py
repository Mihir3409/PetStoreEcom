from django.db import models
from django.contrib.auth.models import User
from Petsapp.models import Pets

# Create your models here.
class Payment(models.Model):
    payment_id = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount_paid = models.CharField(max_length=150)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Orders(models.Model):
        status = (('new','new',),('pending','pending'),('delivered','delivered'),('cancelled','cancelled'))

        states = [
            ('AP','Andra Pradesh'),
            ('AR','Arunachal Pradesh'),
            ('MH','Maharashtra'),
            ('GJ','Gujarat'),
            ('KL','Kerela'),
            ('MP','Madhya Pradesh'),
            ('HP','Himachal Pradesh')
        ]

        user = models.ForeignKey(User, on_delete=models.CASCADE)
        payment = models.ForeignKey(Payment,on_delete=models.SET_NULL, blank=True, null=True)
        order_number = models.CharField(max_length=200)
        first_name = models.CharField(max_length=100)
        last_name = models.CharField(max_length=100)
        phone = models.CharField(max_length=10)
        email = models.EmailField(max_length=200)
        address = models.CharField(max_length=200)
        city = models.CharField(max_length=200)
        state = models.CharField(max_length=200)
        country = models.CharField(max_length=200)
        total = models.CharField(max_length=200)
        status = models.CharField(max_length=200,choices=status,default="New")
        ip = models.CharField(max_length=200)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
              return self.user.first_name
        

class OrderPet(models.Model):
      order_id = models.ForeignKey(Orders,on_delete=models.CASCADE)
      user = models.ForeignKey(User,on_delete=models.CASCADE)
      payment = models.ForeignKey(Payment,on_delete=models.SET_NULL, blank=True, null=True)
      pet = models.ForeignKey(Pets,on_delete=models.CASCADE)
      quantity = models.IntegerField()
      pet_price = models.FloatField()
      is_ordered = models.BooleanField(default=False)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)

      def __str__(self):
            return self.pet.name
      
