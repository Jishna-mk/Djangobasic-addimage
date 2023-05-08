from django.urls import path
from.import views

from .views import ProductListPDF


urlpatterns = [
    # path('',views.first,name='first'),
    path('',views.home,name='home'),
    path('add_product',views.add_product,name='add_product'),
    path('product_list_pdf/', ProductListPDF.as_view(), name='product_list_pdf'),
    
]


