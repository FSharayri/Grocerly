from django.shortcuts import render

# Create your views here.
def home(request):
    pass

def about(request):
    return render(request,'about.html')