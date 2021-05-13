import sqlite3
import parts_list as pl


def sql_push(table_name, parts):
    cur.executemany(f"INSERT INTO {table_name} VALUES(?)", parts)


def database_start():
    # Подключаем бд
    conn = sqlite3.connect('parts.db')

    # Содаём курсор для осуществления SQL запросов
    cur = conn.cursor()

    # Создаём таблицу для каждой комплектующей
    cur.execute("CREATE TABLE IF NOT EXISTS motherboard(obj)")
    cur.execute("CREATE TABLE IF NOT EXISTS cpu(obj)")
    cur.execute("CREATE TABLE IF NOT EXISTS gpu(obj)")
    cur.execute("CREATE TABLE IF NOT EXISTS power_supply(obj)")
    cur.execute("CREATE TABLE IF NOT EXISTS Сase(obj)")
    cur.execute("CREATE TABLE IF NOT EXISTS storage(obj)")
    cur.execute("CREATE TABLE IF NOT EXISTS cooler(obj)")
    cur.execute("CREATE TABLE IF NOT EXISTS wcs(obj)")
    cur.execute("CREATE TABLE IF NOT EXISTS fan(obj)")


def main():
    database_start()


if __name__ == '__main':
    main()
