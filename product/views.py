from typing import List
from django.shortcuts import render
from product.models import Item
from django.views.generic import DetailView, ListView
from django.db.models import Q


# Create your views here.

def home(request):
    items = Item.objects.all()
    context = {
        'items' : items
    }
    return render(request,'home.html',context)


def shirtProduct(request):
    item = Item.objects.all()
    
    items = item.filter(category = "S")
    context = {
        'items' : items
    }
    return render(request,'home.html',context)

def sportwearProduct(request):
    item = Item.objects.all()
    items = item.filter(category = "SW")
    context = {
        'items' : items
    }
    return render(request,'home.html',context)

def outerwearProduct(request):
    item = Item.objects.all()
    items = item.filter(category = "OW")
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
    template_name = 'product.html'

def search(request):
    print("Search function")
    if request.method == "POST":
        searchitems = Item.objects.all()
        print(searchitems)
        search = request.POST.get('search')
        print("search item ", search)
        if search:
            itemsearch = searchitems.filter(Q(title__icontains = search ))
        context ={
            'itemsearch' : itemsearch
        }
        return render (request, 'search.html', context)

def sortItem(request):
    item = Item.objects.all()
    sort = request.GET.get('sort')
    print("sorted",sort)
    if sort == "high-to-low":
        items = item.order_by('-price')
    elif sort == "low-to-high":
        items = item.order_by('price')
    elif sort == "latest":
        items = item.order_by('-created_at')
    else:
        items = item    

    context = {
        'items' : items
    }
    return render(request, 'home.html', context)

# working class based sorting

# class SortResult(ListView):
#     model = Item
#     template_name = "sort.html"

#     def get_queryset(self):
#         item = Item.objects.all()
#         sort = self.request.GET.get('sort')
#         if sort == "high-to-low":
#             object_list = item.order_by('-price')
#         elif sort == "low-to-high":
#             object_list = item.order_by('price')
#         elif sort == "latest":
#             object_list = item.order_by('-created_at')
#         else:
#             object_list = item

#         return object_list    

# ends here