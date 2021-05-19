# posts/urls.py
from django.urls import path
from .partClass import PartClass
from .views import *

urlpatterns = [
    path('', part_list, name='part_list'),
    path('basket', basket, name='basket'),
    path('add/<int:id>/', addToBasket),
    path('delete/<int:id>/', deleteFromBasket),


]