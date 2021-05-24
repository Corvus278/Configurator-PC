from SQLfunctions import getListFromTable


def check_compatibility(table_name, basket):
    """Проверка на совместимость, возвращает список словарей"""
    parts = getListFromTable(table_name)

    # cpu
    if table_name == 'cpu_':
        motherboard = basket.get('motherboard')
        for part in parts:
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
    if table_name == 'gpu':

