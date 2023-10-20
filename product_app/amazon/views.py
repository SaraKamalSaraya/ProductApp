from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse
from amazon.forms import ProductForm,ProductsModelForm
from categories.models import Categories
from amazon.models import Products
from django.contrib.auth.decorators import login_required
from django.views import View

# Create your views here.

def profile(request,id):
    product =  get_object_or_404(Products, pk=id)
    return render(request,'amazon/profile.html',context={'product':product})

def aboutus(request):
    return render(request,'amazon/aboutus.html')

def contactus (request):
    return render(request,'amazon/contactus.html')

def link(request):
    return render(request,'amazon/link.html')

def amazon(request):
    products =  Products.get_all_products()
    return render(request,'amazon/home.html',context={'products':products})

def search (request):
    if request.method == "GET":
        searched = request.GET['searched']
        results = Products.objects.filter(name__istartswith=searched)
        return render(request,'amazon/search.html',{'searched':searched, 'results':results})
    return render(request,'amazon/search.html')

@login_required
def delete(request,id):
    product =  Products.objects.get(id=id)
    current_user = request.user
    product.delete()
    # return HttpResponse(request,'del')
    url = reverse('amazon.amazon')
    return redirect(url)

@login_required
def addProductUsingForms(request):
    form = ProductForm()
    print(request.user.id)
    if request.POST:
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            print(request.POST)
            print(request.FILES)
            # get data from the request body
            name = request.POST['name']
            img=None
            if 'img' in request.FILES:
                img = request.FILES['img']
            description = request.POST['description']
            instock = request.POST['instock']
            price = request.POST['price']
            category = None
            if request.POST['category']:
                category = Categories.objects.get(id=request.POST['category'])
            owner = request.user
            product = Products.objects.create(name=name,img=img,description=description,instock=instock,price=price,category=category,owner=owner)
            return redirect(product.get_profile_url())
    return render(request,'amazon/addProduct.html',{'form':form})

@login_required
def editProductUsingForms(request, id):
    product = Products.get_sepcific_object(id)
    form = ProductsModelForm(instance=product)
    if request.method== 'POST':
        form =  ProductsModelForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect(product.get_profile_url())

    return  render(request, 'amazon/edit.html',
                   context={"form":form})
