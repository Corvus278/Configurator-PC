import sqlite3
import parts_list as pl


def check_values(l):
    """Если элемент списка является списком, он переделывается в строку
    (разделитель - , )"""
    new_list = []
    for i in l:
        if type(i) == list:
            i = ', '.join(i)
        new_list.append(i)
    return new_list


def sql_push(table_name, parts, cur):
    for part in parts:
        keys = ', '.join(part.keys())
        values = part.values()
        values = check_values(values)
        values = tuple(values)
        columns = '?,' * len(values)
        columns = columns[:-1]  # Убираем последнюю запятую
        request = 'INSERT INTO ' + table_name + ' ' + '(' + keys + ')' + \
                  'VALUES (' + columns + ')'
        cur.execute(request, values)


def main():
    # Подключаем бд
    conn = sqlite3.connect('parts.db')
    # Содаём курсор для осуществления SQL запросов
    cur = conn.cursor()

    # Добавляем данные в базу
    sql_push('motherboard', pl.motherboards, cur)
    sql_push('case_', pl.cases, cur)
    sql_push('cpu', pl.cpu, cur)
    sql_push('gpu', pl.gpu, cur)
    sql_push('ram', pl.ram, cur)
    sql_push('power_supply', pl.power_supplies, cur)
    sql_push('storage', pl.storage, cur)
    sql_push('cooler', pl.coolers, cur)
    sql_push('fan', pl.fans, cur)

    # Коммитим и закрываем бд
    conn.commit()
    cur.close()


if __name__ == '__main__':
    main()
