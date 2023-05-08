from django.shortcuts import render,redirect
from django.http import HttpResponse
from.forms import ProductlistForm
from django.contrib import messages

from django.views.generic import View
from django.views.generic import View
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from .models import Productlist

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



# class ProductPDFView(View):
#     def get(self, request, *args, **kwargs):
#         # Create a HttpResponse object with content type PDF
#         response = HttpResponse(content_type='application/pdf')
#         # Set the Content-Disposition header to force download the PDF file
#         response['Content-Disposition'] = 'attachment; filename="products.pdf"'
#         # Create a canvas to draw on
#         pdf_canvas = canvas.Canvas(response)
        
#         # Loop through all_products and draw each product on the canvas
#         y = 750
#         for product in Products:
#             pdf_canvas.drawImage(product.Product_image.url, 50, y, width=100, height=100)
#             pdf_canvas.drawString(200, y+50, product.Product_name)
#             pdf_canvas.drawString(200, y+25, product.Product_category)
#             pdf_canvas.drawString(400, y+50, f"${product.Product_price}")
#             y -= 150
        
#         # Save the PDF canvas and return the HttpResponse object
#         pdf_canvas.save()
#         return response


class ProductListPDF(View):
    def get(self, request, *args, **kwargs):
        # Get all products from the database
        products = Productlist.objects.all()

        # Create a HttpResponse object with content type PDF
        response = HttpResponse(content_type='application/pdf')
        # Set the Content-Disposition header to force download the PDF file
        response['Content-Disposition'] = 'attachment; filename="product_list.pdf"'
        # Create a canvas to draw on
        pdf_canvas = canvas.Canvas(response, pagesize=letter)

        # Set the font size and leading
        pdf_canvas.setFont('Helvetica', 12)
        pdf_canvas.setLineWidth(.3)
        pdf_canvas.setStrokeColorRGB(0.5, 0.5, 0.5)

        # Set the initial y-coordinate
        y = 720

        # Loop through all products and draw each product on the canvas
        for product in products:
            # Draw the product image
            image = product.Product_image.path
            pdf_canvas.drawImage(image, 50, y - 0.5 * inch, width=1.5 * inch, height=1.5 * inch)

            # Draw the product name
            pdf_canvas.drawString(100, y, product.Product_name)
            # Draw the product category
            pdf_canvas.drawString(100, y - 0.25 * inch, product.Product_category)
            # Draw the product price
            pdf_canvas.drawString(100, y - 0.5 * inch, product.Product_price)

            # Decrease the y-coordinate for the next product
            y -= 1.5 * inch

        # Save the PDF canvas and return the HttpResponse object
        pdf_canvas.save()
        return response
