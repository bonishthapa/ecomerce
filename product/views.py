from django.shortcuts import render
from product.models import Item
from django.views.generic import DetailView


# Create your views here.

def home(request):
    items = Item.objects.all()
    context = {
        'items' : items
    }
    return render(request,'home.html',context)

def dashboardIndex(request):
    return render(request,'dashboard/index.html')    

def productView(request,slug):
    item = Item.objects.get(slug=slug)
    return render(request,'product.html')    

class ProductView(DetailView):
    model = Item
    # template = 'product.html'   