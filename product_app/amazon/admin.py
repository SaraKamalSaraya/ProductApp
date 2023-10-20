from django.contrib import admin

# Register your models here.

from amazon.models import Products

admin.site.register(Products)
