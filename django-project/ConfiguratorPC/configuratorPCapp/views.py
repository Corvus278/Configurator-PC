from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .SQLfunctions import getListFromBD
from .partClass import PartClass


def homePage(request):
    CPUList = getListFromBD("cpu")
    PartList = [ PartClass(part) for part in CPUList]
    return render(request, "part_list.html", {"parts": PartList})




