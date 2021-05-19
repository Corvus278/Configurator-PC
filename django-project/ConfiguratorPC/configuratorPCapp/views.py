from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .SQLfunctions import getListFromTable, getFromTable
from .partClass import PartClass
from icecream import ic

def part_list(request):
    CPUDictList = getListFromTable("cpu_")
    partsSQL = [ PartClass(part) for part in CPUDictList]
    return render(request, "part_list.html", {"parts": partsSQL})

def addToBasket(request, id):
    ansDict = getFromTable(id, "cpu_")
    if not request.session['parts']:
        request.session['parts'] = {}

    ic(request.session['parts'])
    request.session['parts']["cpu_"] = ansDict
    request.session.modified = True
    ic(request.session['parts'])
    return redirect('part_list')

def deleteFromBasket(request, id):
    del request.session['parts']["cpu_"]
    request.session.modified = True
    ic(request.session['parts'])
    return redirect('basket')

def basket(request):
    partsBasket = request.session['parts']
    for key, value in partsBasket.items():
        partsBasket[key] = PartClass(value)
    sum_price_min = sum([part.price_min for part in partsBasket.values()])
    sum_price_max = sum([part.price_max for part in partsBasket.values()])
    count = len(partsBasket)
    return render(request, "basket.html", {"parts": partsBasket.items(), "sum_price_min": sum_price_min, "sum_price_max": sum_price_max, "count": count})
