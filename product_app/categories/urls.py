
from django.urls import path
from categories.views import categories,profile

urlpatterns = [
    path('', categories, name='amazon.categories'),
    path('profile/<int:id>', profile, name='categories.profile'),
]