import sqlite3
import parts_list as pl


def sql_push(table_name, parts, cur):
    for part in parts:
        request = "INSERT INTO" + ' ' + table_name + "(dict) VALUES(?)"
        cur.execute(request, (part,))


def main():
    # Подключаем бд
    conn = sqlite3.connect('parts.db')
    # Содаём курсор для осуществления SQL запросов
    cur = conn.cursor()

    # Создаём таблицу для каждой комплектующей
    cur.execute("CREATE TABLE IF NOT EXISTS motherboard(dict TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS cpu(dict TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS gpu(dict TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS ram(dict TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS power_supply(dict TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS case_(dict TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS storage(dict TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS cooler(dict TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS wcs(dict TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS fan(dict TEXT)")

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
