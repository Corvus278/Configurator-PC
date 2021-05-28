from django.shortcuts import render, redirect, reverse
from .SQLfunctions import getListFromTable, getFromTable
from .partClass import PartClass
from icecream import ic


def homePage(request):
    partTypes = {
        "motherboard": "Материнская плата",
        "cpu": "Процессор",
        "gpu": "Видеокарта",
        "ram": "Оперативная память",
        "storage": "Накопитель",
        "power_supply": "Блок питания",
        "case_": "Корпус",
        "cooler": "Охлаждение процессора",
        "fan": "Корпусные вентиляторы",
    }
    return render(request, "index.html", {"partTypes": partTypes.items()})

def part_list(request, partType):
    CPUDictList = getListFromTable(partType)
    partsSQL = [ PartClass(part) for part in CPUDictList]
    return render(request, "part_list.html", {"parts": partsSQL, "partType": partType})


def addToBasket(request, partType, id):
    ansDict = getFromTable(id, partType)
    if 'parts' not in request.session:
        request.session['parts'] = {}

    ic(request.session['parts'])
    request.session['parts'][partType] = ansDict
    request.session.modified = True
    ic(request.session['parts'])
    return redirect(reverse('part_list')+partType)


def deleteFromBasket(request, partType, id):
    del request.session['parts'][partType]
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

