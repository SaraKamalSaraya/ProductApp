

from django.contrib import admin
from django.urls import path,include
from amazon.views import profile,amazon,aboutus,contactus,link,delete,search,addProductUsingForms,editProductUsingForms

urlpatterns = [
    path('', amazon, name='amazon.amazon'),
    path('<int:id>/delete', delete, name='amazon.delete'),
    path('search/', search, name='amazon.search'),
    path('addProduct/', addProductUsingForms, name='amazon.addProduct'),
    path('edit/<int:id>/', editProductUsingForms, name='amazon.edit'),
    path('profile/<int:id>', profile, name='amazon.profile'),
    path('aboutus/', aboutus, name='amazon.aboutus'),
    path('contactus/', contactus, name='amazon.contactus'),
    path('link/', link, name='amazon.link'),
    path('api/', include('amazon.api.urls'))
]