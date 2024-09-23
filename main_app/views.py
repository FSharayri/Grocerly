from django.shortcuts import render
from .models import Item
# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')


def shopping_list(request):
    items = Item.objects.all()
    #Cat.objects.filter(name='Rubber Biscuit')
    #Cat.objects.filter(name__contains='Bis')
    #Cat.objects.filter(age__lte=3)
    #Cat.objects.get(id=1)
    #Cat.objects.order_by('name')
    return render(request, 'items/index.html', {'items':items})
