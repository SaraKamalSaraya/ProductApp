from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from categories.models import Categories
from amazon.models import Products
# Create your views here.

def categories(request):
    categories = Categories.get_all_categories()
    return render(request,'categories/index.html',{'categories':categories})

def profile(request,id):
    category=get_object_or_404(Categories,pk=id)
    products = category.products.all()
    print(products)
    # category_name = category.name
    # products=Products.objects.filter(category==category_name)
    return render(request,'categories/profile.html',{'category':category,'products':products})
