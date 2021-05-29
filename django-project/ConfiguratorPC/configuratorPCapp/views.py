from django.shortcuts import render, redirect, reverse
from .SQLfunctions import getListFromTable, getFromTable
from .partClass import PartClass
from icecream import ic
from django.conf import settings
from .check_compatibility import check_parts_list, check_basket

def homePage(request):
    partTypes = settings.PART_TYPES
    return render(request, "index.html", {"partTypes": partTypes.items()})

def part_list(request, partType):
    if 'parts' not in request.session:
        request.session['parts'] = {}
        request.session.set_expiry(0)
    partsBasket = request.session['parts']

    partsDictList = getListFromTable(partType)
    partsCompList = check_parts_list(partsDictList, partsBasket)
    partsCompList.sort(key=lambda part: not part['compatibility'])
    partsClasses = [ PartClass(part) for part in partsCompList]
    return render(request, "part_list.html", {"parts": partsClasses, "partType": partType})


def addToBasket(request, partType, id):
    if 'parts' not in request.session:
        request.session['parts'] = {}
        request.session.set_expiry(0)

    ansDict = getFromTable(id, partType)
    request.session['parts'][partType] = ansDict
    request.session.modified = True
    return redirect(reverse('part_list')+partType)


def deleteFromBasket(request, partType, id):
    del request.session['parts'][partType]
    request.session.modified = True
    return redirect('basket')


def basket(request):
    if 'parts' not in request.session:
        request.session['parts'] = {}
    partsBasket = request.session['parts']
    partsBasket = check_basket(partsBasket)
    ic(partsBasket)
    for key, value in partsBasket.items():
        partsBasket[key] = PartClass(value)
    sum_price_min = sum([part.price_min for part in partsBasket.values()])
    sum_price_max = sum([part.price_max for part in partsBasket.values()])
    count = len(partsBasket)
    compatibilityAll = all([part.compatibility for part in partsBasket.values()])
    return render(request, "basket.html", {"parts": partsBasket.items(),
                                           "sum_price_min": sum_price_min,
                                           "sum_price_max": sum_price_max,
                                           "count": count,
                                           "compatibilityAll": compatibilityAll})

