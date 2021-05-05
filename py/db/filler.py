import sqlite3
import parts_classes as pc

def sql_push(tabel_name, parts):
    cur.executemany(f"INSERT INTO {tabel_name} VALUES(?)", parts)

def datebase_start():
    # Подключаем бд
    conn = sqlite3.connect('parts.db')

    # Содаём курсор для осуществления SQL запросов
    cur = conn.cursor()

    # Создаём таблицу для каждой комплектующей
    cur.execute("CREATE TABLE IF NOT EXISTS motherboard(obj)")
    cur.execute("CREATE TABLE IF NOT EXISTS cpu(obj)")
    cur.execute("CREATE TABLE IF NOT EXISTS gpu(obj)")
    cur.execute("CREATE TABLE IF NOT EXISTS power_supply(obj)")
    cur.execute("CREATE TABLE IF NOT EXISTS case_(obj)")
    cur.execute("CREATE TABLE IF NOT EXISTS storage(obj)")
    cur.execute("CREATE TABLE IF NOT EXISTS cooler(obj)")
    cur.execute("CREATE TABLE IF NOT EXISTS wcs(obj)")
    cur.execute("CREATE TABLE IF NOT EXISTS fan(obj)")

def main():
    datebase_start()

    # Добавляем блоки питания
    power_supplys = [
        (pc.PowerSupply('Be quiet System Power 9 BN247',
                        'https://www.e-katalog.ru/jpg/1412111.jpg',
                        '4299', '5530', 'ATX', '4', '6')),
        (pc.PowerSupply('Be quiet Pure Power 11 CM BN298',
                        'https://www.e-katalog.ru/jpg/1555252.jpg',
                        '6888', '8360', 'ATX', '4', '6')),
        (pc.PowerSupply('Cooler Master MWE White 230V V2 MPE-6001-ACABW',
                        'https://www.e-katalog.ru/jpg/1764489.jpg',
                        '3620', '4380', 'ATX', '4', '6')),
        (pc.PowerSupply('Super Flower Leadex Platinum SF-850F-14MP',
                        'https://www.e-katalog.ru/jpg/1055052.jpg',
                        '14290', '', 'ATX', '4', '10')),
        (pc.PowerSupply('Seasonic PRIME TX PRIME TX-850',
                        'https://www.e-katalog.ru/jpg/1356256.jpg',
                        '22960', '24990', 'ATX', '6', '10')),
        (pc.PowerSupply('Be quiet Straight Power 11 BN283',
                        'https://www.e-katalog.ru/jpg/1356204.jpg',
                        '11090', '12620', 'ATX', '4', '11')),
        (pc.PowerSupply('Super Flower Leadex Silver SF-750F14MT',
                        'https://www.e-katalog.ru/jpg/1964067.jpg',
                        '8990', '10150', 'ATX', '4', '10')),
        (pc.PowerSupply('Seasonic PRIME PX PRIME PX-1000',
                        'https://www.e-katalog.ru/jpg/1054958.jpg',
                        '28990', '', 'ATX', '8', '12')),
        (pc.PowerSupply('Super Flower Leadex III Gold ARGB SF-750F14RG',
                        'https://www.e-katalog.ru/jpg/1885677.jpg',
                        '10609', '13080', 'ATX', '6', '9')),
        (pc.PowerSupply('Chieftec ECO GPE-500S',
                        'https://www.e-katalog.ru/jpg/866192.jpg',
                        '3038', '3697', 'ATX', '1', '4'))
    ]

    # Добавляем ЦП
    cpu = [
        (pc.CPU('Intel Core i9 Comet Lake i9-10900F BOX',
        'https://www.e-katalog.ru/jpg/1791360.jpg', '27850', '37290',
        'Intel LGA 1200', 'Core i9')
    ]


if __name__ == '__main':
    main()
