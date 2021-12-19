from django.urls import path
from product import views

urlpatterns = [
    path('', views.home, name='index'),
    path('dashboard', views.dashboardIndex, name='dashboard'),
    path('product/<slug>', views.productView, name='product'),
    path('product/class/<slug>', views.ProductView.as_view(),name='product'),
    path('product/search/', views.search, name='search'),
    path('sorting/',views.sortItem, name='sortitem'),
    path('shirts', views.shirtProduct, name='shirt'),
    path('sportwear', views.sportwearProduct, name='sportwear'),
    path('outerwear', views.outerwearProduct, name='outerwear'),


    # path('sorting/',views.SortResult.as_view(), name='sortitem'),
]
