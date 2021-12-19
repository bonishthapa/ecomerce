from django.urls import path
from product import views

urlpatterns = [
    path('', views.home, name='index'),
    path('dashboard', views.dashboardIndex, name='dashboard'),
    path('product/<slug>', views.productView, name='product'),
    path('product/class/<slug>', views.ProductView.as_view(template_name = 'product.html'),name='product'),
]
