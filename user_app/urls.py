from django.urls import path
from.import views

urlpatterns = [
    # path('',views.first,name='first'),
    path('',views.home,name='home'),
    path('add_product',views.add_product,name='add_product')
]
