from django.urls import path
from amazon.api.view import index,product_resource

urlpatterns = [
  path('', index, name='api.index'),
  path('<int:id>', product_resource, name='api.product_resourse')
]