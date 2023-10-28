from django.shortcuts import render
from .models import Pets
from django.http import Http404
from django.db.models import Q
from orders.models import OrderPet

# Create your views here.

def pets_list(request):
    all_products = Pets.objects.all() #query
    context = {
        'objects': all_products
    }
    return render(request, 'Petsapp/list.html', context)

def cat_list(request):
    cat_list = Pets.objects.filter(animal_type='C')
    all_cat_data = {
        'objects': cat_list
    }
    return render(request, 'Petsapp/catlist.html', all_cat_data)

def dog_list(request):
    dog_list = Pets.objects.filter(animal_type='D')
    all_dog_data = {
        'objects': dog_list
    }
    return render(request, 'Petsapp/doglist.html', all_dog_data)

def pet_detail(request,pk):
    query = Pets.objects.get(id=pk)
    context = {
        'objects': query
    }
    
    return render(request, 'Petsapp/pets_detail.html', context)

def search(request):
    if request.method == "GET":
        searched_data = request.GET.get('search')
        if (len(searched_data)==0):
            raise Http404
        else:
            query = (Q(name__icontains=searched_data) | Q(species__icontains=searched_data))
            
            result = Pets.objects.filter(query)
            context = {
                'objects': result
            }
            return render(request,'petsapp/search.html',context)
    else:
        raise Http404
    
def order_history(request):
    user = request.user
    query = OrderPet.objects.filter(user=request.user)
    flag = query.exists()
    status_badge_map = {
        'new':'primary',
        'pending':'warning',
        'delivered':'success',
        'cancelled':'danger'
        }
        # Retriving the order along with associated order item
    orders = OrderPet.objects.filter(user=user).select_related('order_id','pet').order_by('-order_id__created_at')

        # Grouping order by order Number

    order_group = {}
    for order in orders:
        order_number = order.order_id.order_number
        if order_number not in order_group:
            order_group[order_number] = {
                'order_date':order.order_id.created_at.date(),
                'status':order.order_id.status,
                'status_badge_map':status_badge_map.get(order.order_id.status,'secondary'),
                'order_number':order_number,
                'grand_total':0,
                'items':[]
                }

        order_group[order_number]['grand_total'] += order.pet_price
        total_price_per_item = order.quantity * order.pet_price
        order_group[order_number]['items'].append({
            'item_name':order.pet.name,
            'item_price':order.pet_price,
            'quantity':order.quantity,
            'total_price_per_item':total_price_per_item,
            })

    content = {
        'order_group':order_group.values(),
        'flag':flag
        }

    return render(request,'base/order_history.html',content)
