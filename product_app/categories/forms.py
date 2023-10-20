
from django import forms
from models import Categories
from django.core.exceptions import ValidationError


class CategoryForm(forms.Form):
    name = forms.CharField()
    description = forms.Textarea(required=False)
    img = forms.ImageField()

    def clean_name(self):
        found = Categories.objects.filter(name=self.cleaned_data['name']).exists()
        if found:
            raise ValidationError('Category exsists')
        return self.cleaned_data['name']