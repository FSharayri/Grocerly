from django.shortcuts import render
from .models import Item
from .forms import ItemForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class Home(LoginView):
    template_name= 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def shopping_list(request):
    items = Item.objects.filter(user=request.user)
    #Cat.objects.filter(name='Rubber Biscuit')
    #Cat.objects.filter(name__contains='Bis')
    #Cat.objects.filter(age__lte=3)
    #Cat.objects.get(id=1)
    #Cat.objects.order_by('name')
    return render(request, 'items/index.html', {'items':items})


