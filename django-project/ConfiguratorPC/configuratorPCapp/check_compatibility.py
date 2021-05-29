from icecream import ic
from .SQLfunctions import getListFromTable
from django.conf import settings
from icecream import ic

def defineDict(basket):
    partTypes = settings.PART_TYPES
    for key, value in partTypes.items():
        if key not in basket:
            basket[key] = None
    return basket

def check_compatibility(table_name, basket):
    """Проверка на совместимость, возвращает список словарей"""
    parts = getListFromTable(table_name)

    basket = defineDict(basket)
    # cpu
    if table_name == 'cpu':
        # Получение из корзины нужных комплектующих
        motherboard = basket.get('motherboard')
        for part in parts:
            compatibility = True
            if not (motherboard is None):
                compatibility = False
                if part.get('socket') == motherboard.get('socket'):
                    if 'Intel' in part.get('socket'):
                        if part.get('generation') in \
                                motherboard.get('proc_list'):
                            compatibility = True
                    else:
                        # Проверка на совместимость четвёртого поколения
                        if part.get('generation') == '4' and '4' in \
                                motherboard.get('proc_list'):
                            compatibility = True
                        # Остальные поколения
                        if int(part.get('generation')) <= \
                                int(motherboard.get('proc_list')[-1]):
                            compatibility = True
            # Добавляем совместимость в комплектующую
            part.update(compatibility=compatibility)

    # gpu
    elif table_name == 'gpu':
        # Получение из корзины нужных комплектующих
        power_supply = basket.get('power_supply')
        case = basket.get('case')
        # Поверка совместимости
        for part in parts:
            compatibility = True
            if not (power_supply == case):
                try:
                    if int(power_supply.get('connectors_pci_e_8__count')) == 0:
                        compatibility = False
                    else:
                        power_supply.update(connectors_pci_e_8__count=
                                            str(int(power_supply.get(
                                                'connectors_pci_e_8__count')) - 1))
                except Exception as err:
                    ic(err)
                try:
                    if int(part.get('length')) >= int(case.get('gpu_length_max')):
                        compatibility = False
                except Exception as err:
                    ic(err)

            part.update(compatibility=compatibility)

    # ram
    elif table_name == 'ram':
        # Получение из корзины нужных комплектующих
        motherboard = basket.get('motherboard')
        for part in parts:
            compatibility = False
            if not(motherboard is None):
                if part.get('die_count') == motherboard.get('ram_count'):
                    if part.get('ddr') == part.get('ddr'):
                        if part.get('all_volume') == \
                                motherboard.get('ram_gb_count'):
                            if int(part.get('frequency')) <= \
                                    int(motherboard.get('ram_frequency')):
                                if part.get('form') == motherboard.get('form'):
                                    compatibility = True
            part.update(compatibility=compatibility)

    # motherboard
    elif table_name == 'motherboard':
        # Получение из корзины нужных комплектующих
        cpu = basket.get('cpu')
        ram = basket.get('ram')
        case = basket.get('case')
        storage = basket.get('storage')
        cooler = basket.get('cooler')
        for part in parts:
            compatibility = True
            # with cpu
            try:
                if part.get('socket') != cpu.get('socket'):
                    compatibility = False
                if not (cpu.get('generation') in part.get('proc_list')):
                    compatibility = False
            except Exception as err:
                ic(f'm&c: {err}')
            # with ram
            try:
                if part.get('ddr') != ram.get('ddr'):
                    compatibility = False
                if int(part.get('ram_frequency')) < int(ram.get('frequency')):
                    compatibility = False
                if int(part.get('ram_gb_count')) < int(ram.get('all_volume')):
                    compatibility = False
                if int(part.get('ram_count')) < int(ram.get('die_count')):
                    compatibility = False
                if part.get('ram_form') != ram.get('form'):
                    compatibility = False
            except Exception as err:
                ic(f'm&r: {err}')
            try:
                if part.get('form') != case.get('form_motherboard'):
                    compatibility = False
            except Exception as err:
                ic(f'm&case: {err}')
            # with storage
            try:
                if storage.get('form') == 'm2':
                    if int(part.get('m2_count')) == 0:
                        compatibility = False
            except Exception as err:
                ic(f'm&s: {err}')
            # with cooler
            try:
                if not(part.get('socket') in cooler.get('sockets')):
                    compatibility = False
            except Exception as err:
                ic(f'm&cool: {err}')

            part.update(compatibility=compatibility)

    # power supply
    elif table_name == 'power_supply':
        case = basket.get('case')
        gpu = basket.get('gpu')
        for part in parts:
            compatibility = True
            # with case
            try:
                if part.get('form') != case.get('form__power_supply'):
                    compatibility = False
            except Exception as err:
                ic(f'p&c: {err}')
            # with gpu
            try:
                if (int(part.get('connectors_pci_e_8__count'))*8) < \
                        int(eval(gpu.get('pins'))):
                    compatibility = False
            except Exception as err:
                ic(f'p&g: {err}')
            part.update(compatibility=compatibility)

    # storage
    elif table_name == 'storage':
        case = basket.get('case')
        motherboard = basket.get('motherboard')
        for part in parts:
            compatibility = True
            # with motherboard
            try:
                if part.get('form') == 'm2' and motherboard.get('m2_count') == '0':
                    compatibility = False
            except Exception as err:
                ic(f's&m: {err}')
            # with case
            try:
                if part.get('form') != 'm2':
                    if part.get('form') == '2.5' and \
                            int(case.get('sata__2_5__count')) == 0:
                        compatibility = False
                    if part.get('form') == '3.5' and \
                            int(case.get('sata__3_5__count')) == 0:
                        compatibility = False
            except Exception as err:
                ic(f's&c: {err}')
            part.update(compatibility=compatibility)

    # cooler
    elif table_name == 'cooler':
        motherboard = basket.get('motherboard')
        case = basket.get('case')
        for part in parts:
            compatibility = True
            # with motherboard
            try:
                if not(motherboard.get('socket') in part.get('sockets')):
                    compatibility = False
            except Exception as err:
                ic(f'c&m: {err}')
            # with case
            try:
                if int(part.get('height')) > int(case.get('height_cooler')):
                    compatibility = False
            except Exception as err:
                ic(f'c&m: {err}')
            part.update(compatibility=compatibility)

    # case
    elif table_name == 'case_':
        motherboard = basket.get('motherboard')
        gpu = basket.get('gpu')
        cooler = basket.get('cooler')
        power_supply = basket.get('power_supply')
        fan = basket.get('fan')
        for part in parts:
            compatibility = True
            # with motherboard
            try:
                if part.get('form_motherboard') != motherboard.get('form'):
                    compatibility = False
            except Exception as err:
                ic(f'c&m: {err}')
            # with gpu
            try:
                if int(part.get('gpu_length_max')) < int(gpu.get('length')):
                    compatibility = False
            except Exception as err:
                ic(f'c&g: {err}')
            # with cooler
            try:
                if int(part.get('height_cooler')) < int(cooler.get('height')):
                    compatibility = False
            except Exception as err:
                ic(f'c&cool: {err}')
            # with power supply
            try:
                if part.get('power_supply') == '':
                    if part.get('form__power_supply') != power_supply.get('form'):
                        compatibility = False
                    if int(part.get('weight_power_supply')) < \
                       int(power_supply.get('weight')):
                        compatibility = False
                else:
                    compatibility = False
            except Exception as err:
                ic(f'c&p: {err}')
            # with fan (Временное решение)
            try:
                one_form = part.get('fans_front_count').split('/')[0]
                two_form = part.get('fans_front_count').split('/')[-1]
                if not(((int(fan.get('count')) <= int(one_form[0])) and
                       (fan.get('weight') in one_form)) or
                       ((int(fan.get('count')) <= int(two_form[0])) and
                       (fan.get('weight') in two_form))):
                    compatibility = False
            except Exception as err:
                ic(f'c&f: {err}')
            part.update(compatibility=compatibility)

    # fan
    elif table_name == 'fan':
        case = basket.get('case')
        for part in parts:
            compatibility = True
            try:
                one_form = case.get('fans_front_count').split('/')[0]
                two_form = case.get('fans_front_count').split('/')[-1]
                if not (((int(part.get('count')) <= int(one_form[0])) and
                         (part.get('weight') in one_form)) or
                        ((int(part.get('count')) <= int(two_form[0])) and
                         (part.get('weight') in two_form))):
                    compatibility = False
            except Exception as err:
                ic(f'f&c: {err}')
            part.update(compatibility=compatibility)
    return parts
