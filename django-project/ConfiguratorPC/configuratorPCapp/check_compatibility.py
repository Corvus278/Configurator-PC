from icecream import ic
from django.conf import settings

def defineDict(basket):
    partTypes = settings.PART_TYPES
    for key, value in partTypes.items():
        if key not in basket:
            basket[key] = None
    return basket

def check_compatibility(first_part1, second_part1):
    """Проверка на совместимость, возвращает True or False
    Принимает два кортежа (имя комплектующей и словарь в каждом)"""

    name1 = first_part1[0]
    part1 = first_part1[1]
    name2 = second_part1[0]
    part2 = second_part1[1]

    # cpu
    if name1 == 'cpu':
        if name2 == 'motherboard':
            if part1.get('socket') == part2.get('socket'):
                if 'Intel' in part1.get('socket'):
                    if not(part1.get('generation') in part2.get('proc_list')):
                        return False
                else:
                    # Проверка на совместимость четвёртого поколения
                    if part1.get('generation') == '4' and not('4' in
                            part2.get('proc_list')):
                        return False
                    # Остальные поколения
                    if not(int(part1.get('generation')) <=
                            int(part2.get('proc_list')[-1])):
                        return False
            else:
                return False

    # gpu
    elif name1 == 'gpu':
        if name2 == 'power_supply':
            if int(part2.get('connectors_pci_e_8__count')) == 0:
                 return False
            else:
                part2.update(connectors_pci_e_8__count=
                                    str(int(part2.get(
                                        'connectors_pci_e_8__count')) - 1))
        elif name2 == 'case_':
            if int(part1.get('length')) >= int(part2.get('gpu_length_max')):
                 return False

    # ram
    elif name1 == 'ram':
        if name2 == 'motherboard':
            if part1.get('die_count') != part2.get('ram_count'):
                return False
            if part1.get('ddr') != part2.get('ddr'):
                return False
            if part1.get('all_volume') > part2.get('ram_gb_count'):
                return False
            if int(part1.get('frequency')) > int(part2.get('ram_frequency')):
                return False
            if part1.get('form') != part2.get('form'):
                return False

    # motherboard
    elif name1 == 'motherboard':
        # with cpu
        if name2 == 'cpu':
            if part1.get('socket') != part2.get('socket'):
                return False
            if not (part2.get('generation') in part1.get('proc_list')):
                ic(part1.get('generation'))
                ic(part2.get('proc_list'))
                return False
        # with ram
        elif name2 == 'ram':
            if part1.get('ddr') != part2.get('ddr'):
                return False
            if int(part1.get('ram_frequency')) < int(part2.get('frequency')):
                return False
            if int(part1.get('ram_gb_count')) < int(part2.get('all_volume')):
                return False
            if int(part1.get('ram_count')) < int(part2.get('die_count')):
                return False
            if part1.get('ram_form') != part2.get('form'):
                return False
        # with case
        elif name2 == 'case_':
            if part1.get('form') != part2.get('form_motherboard'):
                return False
        # with storage
        elif name2 == 'storage':
            if part2.get('form') == 'm2':
                if int(part1.get('m2_count')) == 0:
                    return False
        # with cooler
        elif name2 == 'cooler':
            if not(part1.get('socket') in part2.get('sockets')):
                return False

    # power supply
    elif name1 == 'power_supply':
        # with case_
        if name2 == 'case':
            if part1.get('form') != part2.get('form__power_supply'):
                return False
        # with gpu
        elif name2 == 'gpu':
            if (int(part1.get('connectors_pci_e_8__count'))*8) < \
                    int(eval(part2.get('pins'))):
                return False

    # storage
    elif name1 == 'storage':
        # with motherboard
        if name2 == 'motherboard':
            if part1.get('form') == 'm2' and part2.get('m2_count') == '0':
                return False
        # with case_
        elif name2 == 'case_':
            if part1.get('form') != 'm2':
                if part1.get('form') == '2.5' and \
                        int(part2.get('sata__2_5__count')) == 0:
                    return False
                if part1.get('form') == '3.5' and \
                        int(part2.get('sata__3_5__count')) == 0:
                    return False

    # cooler
    elif name1 == 'cooler':
        # with motherboard
        if name2 == 'motherboard':
            if not(part2.get('socket') in part1.get('sockets')):
                return False
        # with case_
        elif name2 == 'case_':
            if int(part1.get('height')) > int(part2.get('height_cooler')):
                return False

    # case_
    elif name1 == 'case__':
        # with motherboard
        if name2 == 'motherboard':
            if part1.get('form_motherboard') != part2.get('form'):
                return False
        # with gpu
        elif name2 == 'gpu':
            if int(part1.get('gpu_length_max')) < int(part2.get('length')):
                return False
        # with cooler
        elif name2 == 'cooler':
            if int(part1.get('height_cooler')) < int(part2.get('height')):
                return False
        # with power supply
        elif name2 == 'power_supply':
            if part1.get('power_supply') == '':
                if part1.get('form__power_supply') != part2.get('form'):
                    return False
                if int(part1.get('weight_power_supply')) < \
                   int(part2.get('weight')):
                    return False
            else:
                 return False
        # with fan (Временное решение)
        elif name2 == 'part2':
            one_form = part1.get('part2s_front_count').split('/')[0]
            two_form = part1.get('part2s_front_count').split('/')[-1]
            if not(((int(part2.get('count')) <= int(one_form[0])) and
                   (part2.get('weight') in one_form)) or
                   ((int(part2.get('count')) <= int(two_form[0])) and
                   (part2.get('weight') in two_form))):
                return False
    # fan
    elif name1 == 'fan':
        if name2 == 'case_':
            one_form = part2.get('fans_front_count').split('/')[0]
            two_form = part2.get('fans_front_count').split('/')[-1]
            if not (((int(part1.get('count')) <= int(one_form[0])) and
                     (part1.get('weight') in one_form)) or
                    ((int(part1.get('count')) <= int(two_form[0])) and
                     (part1.get('weight') in two_form))):
                return False
    return True

def check_comp_one2one(partType1, partDict1, partType2, partDict2):
    """Перегрузка оригинальной функции с другими аргументами"""
    return check_compatibility((partType1, partDict1), (partType2, partDict2))

def check_comp_one2one(partFull1, partFull2):
    """Перегрузка оригинальной функции с другими аргументами
    partDictFull - словарь копмлектующей, дополненный полем 'type'"""
    return check_compatibility((partFull1["type"], partFull1), (partFull2["type"], partFull2))

def check_comp_one2list(partType1, partDict1, partType2, partListDict2):
    """Проверка на совместимость partDict1 со ВСЕМИ комплектующими из списка partListDict2
    Возвращает True/False, значения комплектующих не меняются"""

    for partDict2 in partListDict2:
        if not check_comp_one2one(partType1,partDict1,partType2,partDict2):
            return False
    else:
        return True

def check_comp_one2list(partFull1, partFullList):
    for partFullDict2 in partFullList:
        if not check_comp_one2one(partFull1, partFullDict2):
            return False
    else:
        return True

def check_comp_one2dict(partType1, partDict1, basketDict):
    """Проверка одной детали на совместимость с собранной корзиной"""
    for partType, partDict in basketDict.items():
        if not check_comp_one2one(partType1, partDict1, partType, partDict):
            return False
    else:
        return True

def check_comp_one2dict(partFull1, partFullDict):
    """Проверка одной детали на совместимость с собранной корзиной"""
    for partType, partFull2 in partFullDict.items():
        if not check_comp_one2one(partFull1, partFull2):
            return False
    else:
        return True


def set2_comp_one2one(partFull1, partFull2):
    """устанавливает 'compatibility' для обеих деталей"""
    res = check_comp_one2one(partFull1, partFull2)
    partFull1["compatibility"] = res
    partFull2["compatibility"] = res
    return partFull1, partFull2


def set_comp_one2one_ex(partFull1, partFull2):
    """устанавливает 'compatibility' для обеих деталей
    а тажке поле 'unComp' типа set, в случае, если нет совместимости"""
    if check_comp_one2one(partFull1, partFull2):
        partFull1["compatibility"] = True
        partFull2["compatibility"] = True
        partFull1["unComp"] = []
        partFull2["unComp"] = []
    else:
        partFull1["compatibility"] = False
        partFull2["compatibility"] = False
        partFull1["unComp"] = [partFull2]
        partFull2["unComp"] = [partFull1]
    return partFull1, partFull2

def set_comp_one2list(partFull1, partFullList):
    """устанавливает поле compatibility для partFull1 (не для списка)"""
    partFull1["compatibility"] = check_comp_one2list(partFull1, partFullList)
    return partFull1

def set_comp_one2list_ex(partFull1, partFullList):
    """устанавливает поле compatibility для partFull1
    а тажке поле 'unComp' типа set, для списка тех комплектующих, с которыми нет совместимости"""
    unComp = []
    for partFull2 in partFullList:
        if not check_comp_one2one(partFull1, partFull2):
            if unComp.count(partFull2) == 0: # чтобы не повторялись
                unComp.append(partFull2)

    partFull1["compatibility"] = (len(unComp) == 0)
    partFull1["unComp"] = unComp
    return partFull1

def set_comp_one2dict(partFull1, partFullDict):
    """устанавливает поле compatibility для partFull1 (не для словаря)"""
    partFull1["compatibility"] = check_comp_one2dict(partFull1, partFullDict)
    return partFull1

def set_comp_one2dict_ex(partFull1, partFullDict):
    """устанавливает поле compatibility для partFull1
    а тажке поле 'unComp' типа set, для списка тех комплектующих, с которыми нет совместимости"""
    unComp = []
    for partType, partFull2 in partFullDict.items():
        if not check_comp_one2one(partFull1, partFull2):
            print(False)
            if unComp.count(partFull2) == 0: # чтобы не повторялись
                unComp.append(partFull2)

    partFull1["compatibility"] = (len(unComp) == 0)
    partFull1["unComp"] = unComp
    return partFull1

def set_comp_list2list_ex(partFullList1, partFullList2):
    """проверяет и устанавливает совместимость и список несовместимых элементов для ПЕРВОГО списка """
    for i in range(len(partFullList1)):
        partFullList1[i] = set_comp_one2list_ex(partFullList2,partFullList1[i])
    return partFullList1

def set2_comp_list2list_ex(partFullList1, partFullList2):
    """проверяет и устанавливает совместимость и список несовместимых элементов 'каждого с каждым' """
    oldList2 = partFullList2.copy()
    for i in range(len(partFullList2)):
        partFullList2[i] = set_comp_one2list_ex(partFullList1,partFullList2[i])

    for i in range(len(partFullList1)):
        partFullList1[i] = set_comp_one2list_ex(oldList2,partFullList1[i])

    return partFullList1, partFullList2

def set_comp_list2dict_ex(partFullList, partFullDict):
    """проверяет и устанавливает совместимость и список несовместимых элементов для списка """
    for i in range(len(partFullList)):
        partFullList[i] = set_comp_one2dict_ex(partFullList[i], partFullDict)
    return partFullList

def check_parts_list(partsList, basket):
    return set_comp_list2dict_ex(partsList, basket)