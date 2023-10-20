from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from amazon.models import Products
from categories.models import Categories
from django.core.exceptions import ValidationError

class ProductForm (forms.Form):
    name = forms.CharField()
    img = forms.ImageField(required=False)
    description = forms.CharField(required=False)
    instock = forms.IntegerField()
    price = forms.FloatField()
    category = forms.ModelChoiceField(Categories.get_all_categories(),required=False)

    def clean_name(self):
        found = Products.objects.filter(name=self.cleaned_data['name']).exists()
        if found:
            raise ValidationError('Product name exsists')
        return self.cleaned_data['name']



class ProductsModelForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(ProductsModelForm, self).__init__(*args, **kwargs)
        self.fields['owner'].widget.attrs['readonly'] = True