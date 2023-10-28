from django.urls import path
from .import views
urlpatterns = [
    path('pets-list/', views.pets_list, name='pets-list'),
    path('cat-list/', views.cat_list,name='cat-list'),
    path('dog-list/', views.dog_list,name='dog-list'),
    path('pet-detail/<int:pk>',views.pet_detail,name='pet-detail'),
    path('search/', views.search,name="search"),
    path('my_orders/', views.order_history,name="my_orders"),
]
