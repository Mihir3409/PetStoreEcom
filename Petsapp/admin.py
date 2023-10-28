from django.contrib import admin
from .models import Pets
from django.utils.html import format_html
from orders.models import Orders,Payment,OrderPet
from cart.models import cart

class OrderCustom(admin.ModelAdmin):
    list_display = ['user','status']

class PaymentCustom(admin.ModelAdmin):
    list_display = ['payment_id','status']


class CustomAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'age', 'price', 'species', 'description', 'img_display' ]
    search_fields=['age', 'species']
    list_filter=['animal_type','gender']
    list_per_page = 3
    
    def img_display(self,obj):
        return format_html('<img src={} width="90" height="90" />',obj.image.url)
    
# Register your models here.
admin.site.register(Pets, CustomAdmin)
admin.site.register(cart)
admin.site.register(Orders, OrderCustom)
admin.site.register(Payment, PaymentCustom)
admin.site.register(OrderPet)


