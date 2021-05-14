import sqlite3
import parts_list as pl


def database_start():
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
    cur.execute("CREATE TABLE IF NOT EXISTS case(dict TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS storage(dict TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS cooler(dict TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS wcs(dict TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS fan(dict TEXT)")


def sql_push(table_name, parts):
    for part in parts:
        cur.execute(f"INSERT INTO {table_name}(dict) VALUES({part})")


def main():
    database_start()
    sql_push('motherboard', pl.motherboards)
    sql_push('cpu', pl.cpu)
    sql_push('gpu', pl.gpu)
    sql_push('ram', pl.ram)
    sql_push('power_supply', pl.power_supply)
    sql_push('storage', pl.storage)
    sql_push('cooler', pl.coolers)
    sql_push('fan', pl.fans)


if __name__ == '__main':
    main()
