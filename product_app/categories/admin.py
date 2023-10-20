from django.contrib import admin

# Register your models here.

from categories.models import Categories

admin.site.register(Categories)