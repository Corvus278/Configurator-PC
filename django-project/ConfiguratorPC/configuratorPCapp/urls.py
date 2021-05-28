# posts/urls.py
from django.urls import path
from .partClass import PartClass
from .views import *

urlpatterns = [
    path('', homePage),
    path('home', homePage, name='home'),
    path('part_list/<str:partType>', part_list, name='part_list'),
    path('part_list/', part_list, name='part_list'),
    path('basket', basket, name='basket'),
    path('add/<str:partType>/<int:id>/', addToBasket),
    path('delete/<str:partType>/<int:id>/', deleteFromBasket),
]