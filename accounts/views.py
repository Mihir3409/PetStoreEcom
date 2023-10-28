from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib import messages
from Petsapp.views import pets_list
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy

# Create your views here.

def register(request):
    if request.method == "GET":
        form = RegistrationForm()
        return render(request, 'base/register.html', {'form':form})
    
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,'Congratulations you have registered sucessfully as '+ username)
            return redirect(pets_list)
        else:
            messages.error(request,'Invalid Data ')
            return render(request,'base/register.html',{'form':form})
        
class MyLoginView(LoginView):
    def form_valid(self, form):
        messages.success(self.request,"Logged In Successfully")
        return super().form_valid(form)
        
    def form_invalid(self, form):
        messages.error(self.request,"Invalid Crediantials")
        return super().form_invalid(form)
    

class MyLogoutView(LogoutView):
    def get_next_page(self):
        return reverse_lazy('home')
    
    

    