from django.shortcuts import render,redirect
from django.http import HttpResponse
from.forms import ProductlistForm
from django.contrib import messages
from.models import Productlist

# Create your views here.
# def first(request):
#     return HttpResponse("Hello world")

def home(request):
      Products=Productlist.objects.all().order_by("-Product_ID")
      return render(request,"home_page.html",{"all_products":Products})

def add_product(request):
    form=ProductlistForm()
    if request.method=='POST':
        form=ProductlistForm(request.POST,request.FILES)
        if form.is_valid():
            form_data=form.save()
            form_data.save()
            messages.info(request,"Product added succesfully")
            return redirect("home")
        else:
            form = ProductlistForm()
            messages.info(request,"Product not added!")
            return redirect('add_product')
        
    return render(request,"add_product.html",{"add_form":form})