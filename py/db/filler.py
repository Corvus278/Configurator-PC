import sqlite3
import parts_classes as pc

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
    cur.execute("CREATE TABLE IF NOT EXISTS case_(obj)")
    cur.execute("CREATE TABLE IF NOT EXISTS storage(obj)")
    cur.execute("CREATE TABLE IF NOT EXISTS cooler(obj)")
    cur.execute("CREATE TABLE IF NOT EXISTS wcs(obj)")
    cur.execute("CREATE TABLE IF NOT EXISTS fan(obj)")

def main():
    database_start()

    # Создаём блоки питания
    power_supplies = [
        (pc.PowerSupply('Be quiet System Power 9 BN247',
                        'https://www.e-katalog.ru/jpg/1412111.jpg',
                        'https://www.e-katalog.ru/BE-QUIET-BN247.htm',
                        '4299', '5530', 'ATX', '4', '6')),
        (pc.PowerSupply('Be quiet Pure Power 11 CM BN298',
                        'https://www.e-katalog.ru/jpg/1555252.jpg',
                        'https://www.e-katalog.ru/BE-QUIET-BN298.htm'
                        '6888', '8360', 'ATX', '4', '6')),
        (pc.PowerSupply('Cooler Master MWE White 230V V2 MPE-6001-ACABW',
                        'https://www.e-katalog.ru/jpg/1764489.jpg',
                        'https://www.e-katalog.ru/COOLER-MASTER-MPE-6001-ACABW.htm',
                        '3620', '4380', 'ATX', '4', '6')),
        (pc.PowerSupply('Super Flower Leadex Platinum SF-850F-14MP',
                        'https://www.e-katalog.ru/jpg/1055052.jpg',
                        'https://www.e-katalog.ru/SUPER-FLOWER-SF-850F-14MP.htm',
                        '14290', '', 'ATX', '4', '10')),
        (pc.PowerSupply('Seasonic PRIME TX PRIME TX-850',
                        'https://www.e-katalog.ru/jpg/1356256.jpg',
                        'https://www.e-katalog.ru/SEASONIC-PRIME-TX-850.htm',
                        '22960', '24990', 'ATX', '6', '10')),
        (pc.PowerSupply('Be quiet Straight Power 11 BN283',
                        'https://www.e-katalog.ru/jpg/1356204.jpg',
                        'https://www.e-katalog.ru/BE-QUIET-BN283.htm',
                        '11090', '12620', 'ATX', '4', '11')),
        (pc.PowerSupply('Super Flower Leadex Silver SF-750F14MT',
                        'https://www.e-katalog.ru/jpg/1964067.jpg',
                        'https://www.e-katalog.ru/SUPER-FLOWER-SF-750F14MT.htm',
                        '8990', '10150', 'ATX', '4', '10')),
        (pc.PowerSupply('Seasonic PRIME PX PRIME PX-1000',
                        'https://www.e-katalog.ru/jpg/1054958.jpg',
                        'https://www.e-katalog.ru/SEASONIC-PRIME-PX-1000.htm',
                        '28990', '', 'ATX', '8', '12')),
        (pc.PowerSupply('Super Flower Leadex III Gold ARGB SF-750F14RG',
                        'https://www.e-katalog.ru/jpg/1885677.jpg',
                        'https://www.e-katalog.ru/SUPER-FLOWER-SF-750F14RG.htm',
                        '10609', '13080', 'ATX', '6', '9')),
        (pc.PowerSupply('Chieftec ECO GPE-500S',
                        'https://www.e-katalog.ru/jpg/866192.jpg',
                        'https://www.e-katalog.ru/CHIEFTEC-GPE-500S.htm',
                        '3038', '3697', 'ATX', '1', '4'))
    ]

    # Создаём ЦП
    cpu = [
        (pc.CPU('Intel Core i9 Comet Lake i9-10900F BOX',
                'https://www.e-katalog.ru/jpg/1791360.jpg',
                'https://www.e-katalog.ru/INTEL-I9-10900F-BOX.htm',
                '27850', '37290', 'Intel LGA 1200', 'Core i9', '10')),
        (pc.CPU('AMD Ryzen 9 Vermeer 5900X OEM',
                'https://www.e-katalog.ru/AMD-5900X-OEM.htm',
                'https://www.e-katalog.ru/jpg/1884974.jpg',
                '45517', '57366', 'AMD AM4', 'Ryzen 9', '5')),
        (pc.CPU('Intel Core i7 Comet Lake i7-10700 OEM',
                'https://www.e-katalog.ru/jpg/1789394.jpg',
                'https://www.e-katalog.ru/INTEL-I7-10700-OEM.htm',
                '23229', '33514', 'Intel LGA 1200', 'Core i7', '10')),
        (pc.CPU('AMD Ryzen 7 Matisse 3700X BOX',
                'https://www.e-katalog.ru/jpg/1485973.jpg',
                'https://www.e-katalog.ru/AMD-3700X-BOX.htm',
                '24546', '31733', 'AMD AM4', 'Ryzen 7', '3')),
        (pc.CPU('Intel Core i7 Rocket Lake i7-11700 BOX',
                'https://www.e-katalog.ru/jpg/1983507.jpg',
                'https://www.e-katalog.ru/INTEL-I7-11700-BOX.htm',
                '27586', '37780', 'Intel LGA 1200', 'Core i7', '11')),
        (pc.CPU('Intel Core i9 Rocket Lake i9-11900 BOX',
                'https://www.e-katalog.ru/jpg/1983524.jpg',
                'https://www.e-katalog.ru/INTEL-I9-11900-BOX.htm',
                '35310', '44844', 'Intel LGA 1200', 'Core i9', '11')),
        (pc.CPU('AMD Ryzen 7 Renoir 4750G PRO OEM',
                'https://www.e-katalog.ru/jpg/1845919.jpg',
                'https://www.e-katalog.ru/AMD-4750G-PRO-OEM.htm',
                '25597', '29862', 'AMD AM4', 'Ryzen 7', '4')),
        (pc.CPU('AMD Ryzen 7 Vermeer 5800X BOX',
                'https://www.e-katalog.ru/jpg/1884979.jpg',
                'https://www.e-katalog.ru/AMD-5800X-BOX.htm',
                '34480', '44536', 'AMD AM4', 'Ryzen 7', '5')),
        (pc.CPU('Intel Core i5 Rocket Lake i5-11400F BOX',
                'https://www.e-katalog.ru/jpg/1983474.jpg',
                'https://www.e-katalog.ru/INTEL-I5-11400F-BOX.htm',
                '15724', '17997', 'Intel LGA 1200', 'Core i5', '11')),
        (pc.CPU('AMD Ryzen 5 Renoir 4650G PRO OEM',
                'https://www.e-katalog.ru/jpg/1845914.jpg',
                'https://www.e-katalog.ru/AMD-4650G-PRO-OEM.htm',
                '18580', '23000', 'AMD AM4', 'Ryzen 5', '4')),
        (pc.CPU('Intel Core i5 Comet Lake i5-10400F BOX',
                'https://www.e-katalog.ru/jpg/1789393.jpg',
                'https://www.e-katalog.ru/INTEL-I5-10400F-BOX.htm',
                '12450', '19890', 'Intel LGA 1200', 'Core i5', '10')),
        (pc.CPU('AMD Ryzen 5 Matisse 3600 BOX',
                'https://www.e-katalog.ru/jpg/1485969.jpg',
                'https://www.e-katalog.ru/AMD-3600-BOX.htm',
                '13500', '18620', 'AMD AM4', 'Ryzen 5', '3')),
        (pc.CPU('AMD Ryzen 9 Vermeer 5950X OEM',
                'https://www.e-katalog.ru/jpg/1884974.jpg',
                'https://www.e-katalog.ru/AMD-5950X-OEM.htm',
                '74250', '104934', 'AMD AM4', 'Ryzen 9', '5'))
    ]

    # Создаём Мат. платы
    motherboards = [
                    (pc.Motherboard('ASRock B450 Steel Legend',
                                    'https://www.e-katalog.ru/jpg/1504480.jpg',
                                    'https://www.e-katalog.ru/ASROCK-B450-STEEL-LEGEND.htm',
                                    '7270', '8370', 'ATX', 'AMD AM4', '2-5',
                                    '24', '2', '1xSATA/PCI-E 2x, 1xPCI-E 4x',
                                    '6', '', '3', '4', '4400', '128', '4')),
                    (pc.Motherboard('Asus TUF GAMING B450M-PLUS II',
                                    'https://www.e-katalog.ru/jpg/1898515.jpg',
                                    'https://www.e-katalog.ru/ASUS-TUF-GAMING-B450M-PLUS-II.htm',
                                    '7560', '8559', 'micro-ATX', 'AMD AM4',
                                    '1-4-5', '24', '1', '1xSATA/PCI-E 4x', '6',
                                    '3', '4', '4400', '128', '4')),
                    (pc.Motherboard('Asus TUF B450M-PRO GAMING',
                                    'https://www.e-katalog.ru/jpg/1478832.jpg',
                                    'https://www.e-katalog.ru/ASUS-TUF-B450M-PRO-GAMING.htm',
                                    '7720', '8700', 'micro-ATX', 'AMD AM4',
                                    '1-4-5', '24', '2',
                                    '1xSATA/PCI-E 4x, 1xSATA/PCI-E', '6', '3',
                                    '4', '3533', '64', '4')),
                    (pc.Motherboard('MSI B450 TOMAHAWK MAX II',
                                    'https://www.e-katalog.ru/jpg/1986522.jpg',
                                    'https://www.e-katalog.ru/MSI-B450-TOMAHAWK-MAX-II.htm',
                                    '7338', '9220', 'ATX', 'AMD AM4', '1-3',
                                    '24', '1', '1xSATA/PCI-E 4x', '6', '6',
                                    '4', '4133', '128', '4')),
                    (pc.Motherboard('Gigabyte B450 AORUS ELITE rev. 1.0',
                                    'https://www.e-katalog.ru/jpg/1431618.jpg',
                                    'https://www.e-katalog.ru/GIGABYTE-B450-AORUS-ELITE-REV--1-0.htm',
                                    '7590', '8390', 'ATX', 'AMD AM4', '1-5',
                                    '24', '2', '1xSATA/PCI-E 4x, 1xPCI-E 2x',
                                    '1xSATA/PCI-E 4x, 1xPCI-E 2x', '6', '4',
                                    '4', '3600', '64', '4'))
    ]




if __name__ == '__main':
    main()
