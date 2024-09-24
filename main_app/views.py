from django.shortcuts import render, redirect
from .models import Item , CATEGORY_CHOICES
from .forms import ItemForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# views.
class Home(LoginView):
    template_name= 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def shopping_list(request):
    items = Item.objects.filter(user=request.user, purchased = False)
    categories = []
    for item in items:
        categories.append(item.get_full_category_name())
    return render(request, 'items/index.html', {'items':items, 'categories': categories})

@login_required
def shopping_list_by_cat(request,cat):
    items = Item.objects.filter(user=request.user, purchased = False)
    categories = []
    for item in items:
        categories.append(item.get_full_category_name())

    def get_category_key_by_name(category_name): # you have to own pride in such a method... ! 
        for key, value in CATEGORY_CHOICES:
            if value == category_name:
                return key
    
    items_by_cat = items.filter(category = get_category_key_by_name(cat))
    return render(request, 'items/index-cat.html', {'items':items_by_cat, 'categories': categories})

@login_required
def history(request):
    items = Item.objects.filter(user=request.user, purchased = True)
    return render(request, 'items/history.html', {'items':items})

@login_required
def item_detail(request, item_id):
    item = Item.objects.get(id=item_id)
    item_form = ItemForm()
    return render(request,'items/detail.html',{ 
        'item':item, 'item_form': item_form,
    })

@login_required
def mark_purchased(request, item_id):
    item = Item.objects.get(id=item_id)
    item.purchased = not item.purchased
    item.save()
    if not item.purchased:
        return redirect('history')
    else:
        return redirect('shopping-list')

#C
class ItemCreate(LoginRequiredMixin,CreateView):
    model = Item
    fields = ['name', 'quantity', 'category']
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

#U
class ItemUpdate(LoginRequiredMixin,UpdateView):
    model = Item
    fields =  ['name', 'quantity', 'category', 'purchased']

#D
class ItemDelete(LoginRequiredMixin,DeleteView):
    model = Item
    success_url = '/items/'
    #Cat.objects.filter(name='Rubber Biscuit')
    #Cat.objects.filter(name__contains='Bis')
    #Cat.objects.filter(age__lte=3)
    #Cat.objects.get(id=1)
    #Cat.objects.order_by('name')


def signup(request):
    error_message = ''
    # post 
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request,user)
            return redirect('shopping-list')
        else: 
            error_message= 'Invalid sign up - try again'
    # get or sign up is invalid 
    form = UserCreationForm()
    context= {'form':form ,'error_message': error_message}
    return render(request, 'signup.html', context)
    