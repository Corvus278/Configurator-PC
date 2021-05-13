import parts_classes as pc


# Блоки питания
power_supplies = [
    (pc.PowerSupply('Be quiet System Power 9 BN247',
                    'https://www.e-katalog.ru/jpg/1412111.jpg',
                    'https://www.e-katalog.ru/BE-QUIET-BN247.htm',
                    '4299', '5530', 'ATX', '4', '6')),
    (pc.PowerSupply('Be quiet Pure Power 11 CM BN298',
                    'https://www.e-katalog.ru/jpg/1555252.jpg',
                    'https://www.e-katalog.ru/BE-QUIET-BN298.htm',
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

# ЦП
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

# Мат. платы
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
                                '4', '3600', '64', '4')),
                (pc.Motherboard('MSI H410M-A PRO',
                                'https://www.e-katalog.ru/jpg/1804482.jpg',
                                'https://www.e-katalog.ru/MSI-H410M-A-PRO.htm',
                                '5500', '7756', 'micro-ATX',
                                'Intel LGA 1200', '10', '24', '1',
                                '1xSATA/PCI-E 4x', '4', '2', '4', '2933',
                                '64', '2')),
                (pc.Motherboard('Asus PRIME H410M-K',
                                'https://www.e-katalog.ru/jpg/1793206.jpg',
                                'https://www.e-katalog.ru/ASUS-PRIME-H410M-K.htm',
                                '5295', '7099', 'micro-ATX',
                                'Intel LGA 1200', '10 pentium gold celeron',
                                '24', '0', '', '4', '2', '4', '2933', '64',
                                '2')),
                (pc.Motherboard('ASRock H470M-HDV',
                                'https://www.e-katalog.ru/jpg/1968362.jpg',
                                'https://www.e-katalog.ru/ASROCK-H470M-HDV.htm',
                                '5390', '6220', 'micro-ATX',
                                'Intel LGA 1200', '10', '24', '0', '', '4',
                                '3', '4', '2933', '64', '2')),
                (pc.Motherboard('Gigabyte H410M S2',
                                'https://www.e-katalog.ru/jpg/1863797.jpg',
                                'https://www.e-katalog.ru/GIGABYTE-H410M-S2.htm',
                                '5560', '6590', 'micro-ATX',
                                'Intel LGA 1200', '10 pentium', '24', '0',
                                '', '4', '2', '4', '2933', '64', '2')),
                (pc.Motherboard('ASRock B460 Steel Legend',
                                'https://www.e-katalog.ru/jpg/1792678.jpg',
                                'https://www.e-katalog.ru/ASROCK-B460-STEEL-LEGEND.htm',
                                '8990', '10990', 'ATX', 'Intel LGA 1200',
                                '10', '24', '2',
                                '1xSATA/PCI-E 4x, 1xPCI-E 4x', '6', '7',
                                '4', '2933', '128', '4'))
]

# GPU
gpu = [
       (pc.GPU('MSI GeForce GTX 1660 SUPER VENTUS XS OC',
               'https://www.e-katalog.ru/jpg/1681945.jpg',
               'https://www.e-katalog.ru/MSI-GEFORCE-GTX-1660-SUPER-VENTUS-XS-OC.htm',
               '69020', '', 'PCI-E v3.0', '8', '204')),
       (pc.GPU('MSI Radeon RX 6900 XT GAMING X TRIO 16G',
               'https://www.e-katalog.ru/jpg/1972091.jpg',
               'https://www.e-katalog.ru/MSI-RADEON-RX-6900-XT-GAMING-X-TRIO-16G.htm',
               '176', '', 'PCI-E v4.0', '8*3', '324')),
       (pc.GPU('XFX Radeon RX 6900 XT RX-69XTACBD9',
               'https://www.e-katalog.ru/jpg/1987553.jpg',
               'https://www.e-katalog.ru/XFX-RADEON-RX-6900-XT-RX-69XTACBD9.htm',
               '175990', '', '	PCI-E v4.0', '8*2', '340')),
       (pc.GPU('ASRock Radeon RX 6900 XT Phantom Gaming D 16G OC',
               'https://www.e-katalog.ru/jpg/1924771.jpg',
               'https://www.e-katalog.ru/ASROCK-RADEON-RX-6900-XT-PHANTOM-GAMING-D-16G-OC.htm',
               '168300', '', 'PCI-E v4.0', '8*3', '330')),
       (pc.GPU('Gigabyte Radeon RX 6700 XT EAGLE 12G',
               'https://www.e-katalog.ru/jpg/1977441.jpg',
               'https://www.e-katalog.ru/GIGABYTE-RADEON-RX-6700-XT-EAGLE-12G.htm',
               '118750', '', 'PCI-E v4.0', '6+8', '282')),
       (pc.GPU('Gigabyte GeForce RTX 3080 AORUS XTREME WATERFORCE 10G',
               'https://www.e-katalog.ru/jpg/1910527.jpg',
               'https://www.e-katalog.ru/GIGABYTE-GEFORCE-RTX-3080-AORUS-XTREME-WATERFORCE-10G.htm',
               '269990', '', 'PCI-E v4.0', '8*2', '252')),
       (pc.GPU('INNO3D GeForce RTX 3080 ICHILL X3',
               'https://www.e-katalog.ru/jpg/1883177.jpg',
               'https://www.e-katalog.ru/INNO3D-GEFORCE-RTX-3080-ICHILL-X3.htm',
               '249990', '', 'PCI-E v4.0', '8*2', '300')),
       (pc.GPU('MSI GeForce RTX 3060 VENTUS 2X 12G OC',
               'https://www.e-katalog.ru/jpg/1941016.jpg',
               'https://www.e-katalog.ru/MSI-GEFORCE-RTX-3060-VENTUS-2X-12G-OC.htm',
               '88000', '115900', 'PCI-E v4.0', '8', '235')),
       (pc.GPU('MSI GeForce RTX 2060 VENTUS 6G OC',
               'https://www.e-katalog.ru/jpg/1500206.jpg',
               'https://www.e-katalog.ru/MSI-GEFORCE-RTX-2060-VENTUS-6G-OC.htm',
               '81990', '', 'PCI-E v3.0', '8', '226')),
       (pc.GPU('Asus GeForce RTX 3060 ROG Strix Gaming OC 12GB',
               'https://www.e-katalog.ru/jpg/1941067.jpg',
               'https://www.e-katalog.ru/ASUS-GEFORCE-RTX-3060-ROG-STRIX-GAMING-OC-12GB.htm',
               '108285', '', 'PCI-E v4.0', '8', '300'))
]

# RAM
ram = [
       (pc.RAM('HyperX HX436C17FB3AK2/16',
               'https://www.e-katalog.ru/jpg/1638285.jpg',
               'https://www.e-katalog.ru/HYPERX-HX436C17FB3AK2-16.htm',
               '9438', '10980', '2', '4', '16', '3600')),
       (pc.RAM('Corsair CMW16GX4M2C3600C18',
               'https://www.e-katalog.ru/jpg/1374369.jpg',
               'https://www.e-katalog.ru/CORSAIR-CMW16GX4M2C3600C18.htm',
               '10890', '12448', '2', '4', '16', '3600')),
       (pc.RAM('G.Skill F4-3600C18D-16GTZR',
               'https://www.e-katalog.ru/jpg/1132031.jpg',
               'https://www.e-katalog.ru/G-SKILL-F4-3600C18D-16GTZR.htm',
               '11610', '12560', '2', '4', '16', '3600')),
       (pc.RAM('HyperX Fury Black DDR4 2x8Gb',
               'https://www.e-katalog.ru/jpg/1663620.jpg',
               'https://www.e-katalog.ru/HYPERX-HX437C19FB3K2-16.htm',
               '8789', '10330', '2', '4', '16', '3733')),
       (pc.RAM('Kingston KVR ValueRAM DDR4 1x8Gb',
               'https://www.e-katalog.ru/jpg/1686416.jpg',
               'https://www.e-katalog.ru/KINGSTON-KVR29N21S8-8.htm',
               '3609', '4433', '1', '4', '8', '2933')),
       (pc.RAM('Patriot Signature DDR4 1x8Gb',
               'https://www.e-katalog.ru/jpg/1107298.jpg',
               'https://www.e-katalog.ru/PATRIOT-PSD48G240082.htm',
               '3370', '4133', '1', '4', '8', '2400')),
       (pc.RAM('Samsung DDR4 1x8Gb',
               'https://www.e-katalog.ru/jpg/589635.jpg',
               'https://www.e-katalog.ru/SAMSUNG-M378A1G43DB0-CPB.htm',
               '3300', '', '1', '4', '8', '2133')),
       (pc.RAM('Corsair Vengeance RGB Pro DDR4 2x16Gb',
               'https://www.e-katalog.ru/jpg/1685067.jpg',
               'https://www.e-katalog.ru/CORSAIR-CMW32GX4M2Z3600C18.htm',
               '18789', '21529', '2', '4', '32', '3600')),
       (pc.RAM('HyperX Fury DDR4 RGB 2x16Gb',
               'https://www.e-katalog.ru/jpg/1685287.jpg',
               'https://www.e-katalog.ru/HYPERX-HX437C19FB3AK2-32.htm',
               '18900', '19499', '2', '4', '32', '3733')),
       (pc.RAM('HyperX Predator RGB DDR4 2x16Gb',
               'https://www.e-katalog.ru/jpg/1685325.jpg',
               'https://www.e-katalog.ru/HYPERX-HX436C17PB3AK2-32.htm',
               '19790', '', '2', '4', '32', '3600'))
]

# Накопители
storage = [
    (pc.Storage('SSD WD Green SSD M.2 WDS240G2G0B',
                'https://www.e-katalog.ru/jpg/947253.jpg',
                'https://www.e-katalog.ru/WD-WDS240G2G0B.htm',
                '2589', '3999', 'm2', m2_form='80', m2_interface='SATA3')),
    (pc.Storage('SmartBuy SB240GB-RVVL3-25SAT3',
                'https://www.e-katalog.ru/jpg/1431357.jpg',
                'https://www.e-katalog.ru/SMARTBUY-SB240GB-RVVL3-25SAT3.htm',
                '2734', '3818', '2.5', connector='SATA')),
    (pc.Storage('SSD Patriot P300 M.2 P300P256GM28',
                'https://www.e-katalog.ru/jpg/1741997.jpg',
                'https://www.e-katalog.ru/PATRIOT-P300P256GM28.htm',
                '2749', '3906', 'm2', m2_form='80',
                m2_interface='PCI-E 3.0 4x')),
    (pc.Storage('SSD SmartBuy Stream E13T Pro SBSSD-128GT-PH13P-M2P4',
                'https://www.e-katalog.ru/jpg/1859186.jpg',
                'https://www.e-katalog.ru/SMARTBUY-SBSSD-128GT-PH13P-M2P4.htm',
                '1969', '2440', 'm2', m2_form='80',
                m2_interface='PCI-E 3.0 4x')),
    (pc.Storage('SSD SmartBuy Stream E13T Pro SBSSD-128GT-PH13P-M2P4',
                'https://www.e-katalog.ru/jpg/1507857.jpg',
                'https://www.e-katalog.ru/SAMSUNG-MZ-V7S250BW.htm',
                '4170', '7990', 'm2', m2_form='80',
                m2_interface='PCI-E 3.0 4x')),
    (pc.Storage('Seagate BarraCuda Compute 2.5" ST1000LM048 1 ТБ',
                'https://www.e-katalog.ru/jpg/979798.jpg',
                'https://www.e-katalog.ru/SEAGATE-ST1000LM048.htm',
                '3125', '3970', '2.5', connector='SATA')),
    (pc.Storage('WD Blue 2.5" WD10SPZX 1 ТБ 128/5400',
                'https://www.e-katalog.ru/jpg/1166573.jpg',
                'https://www.e-katalog.ru/WD-WD10SPZX.htm',
                '3190', '4600', '2.5', connector='SATA')),
    (pc.Storage('Seagate Mobile HDD 2.5" ST1000LM035 1 ТБ',
                'https://www.e-katalog.ru/jpg/831783.jpg',
                'https://www.e-katalog.ru/SEAGATE-ST1000LM035.htm',
                '3340', '', '2.5', connector='SATA')),
    (pc.Storage('WD Green WD10EZRX 1 ТБ',
                'https://www.e-katalog.ru/jpg/761566.jpg',
                'https://www.e-katalog.ru/WD-WD10EZRX.htm',
                '12042', '', '3.5', connector='SATA')),
    (pc.Storage('Seagate FireCuda ST1000DX002 1 ТБ',
                'https://www.e-katalog.ru/jpg/927666.jpg',
                'https://www.e-katalog.ru/SEAGATE-ST1000DX002.htm',
                '8510', '', '3.5', connector='SATA')),
]

# Куллеры
coolers = [
    (pc.Cooler('ID-COOLING SE-224-XT ARGB V2',
               'https://www.e-katalog.ru/jpg/1901724.jpg',
               'https://www.e-katalog.ru/ID-COOLING-SE-224-XT-ARGB-V2.htm',
               '2170', '2380', ['AMD AM4', 'Intel 1150', 'Intel 1155',
                                'Intel 1156', 'Intel 2011', 'Intel 2011 v3',
                                'Intel 2066', 'Intel 1151', 'Intel 1151 v2',
                                'Intel 1200'], '154', '73')),
    (pc.Cooler('ID-COOLING SE-234-ARGB',
               'https://www.e-katalog.ru/jpg/1751027.jpg',
               'https://www.e-katalog.ru/ID-COOLING-SE-234-ARGB.htm',
               '2380', '3499', ['AMD AM4', 'Intel 1150', 'Intel 1155',
                                'Intel 1156', 'Intel 2011', 'Intel 2011 v3',
                                'Intel 2066', 'Intel 1151', 'Intel 1151 v2',
                                'Intel 1200'], '154', '88')),
    (pc.Cooler('PCCooler GI-X6B V2',
               'https://www.e-katalog.ru/jpg/2001403.jpg',
               'https://www.e-katalog.ru/PCCOOLER-GI-X6B-V2.htm',
               '1760', '2000', ['AMD AM4', 'Intel 1150', 'Intel 1155',
                                'Intel 1156', 'Intel 2011', 'Intel 2011 v3',
                                'Intel 2066', 'Intel 1151', 'Intel 1151 v2',
                                'Intel 1200'], '148', '85')),
    (pc.Cooler('PCCooler GI-H58U CORONA',
               'https://www.e-katalog.ru/jpg/1639445.jpg',
               'https://www.e-katalog.ru/PCCOOLER-GI-X6B-V2.htm',
               '2978', '4010', ['AMD AM4', 'Intel 1150', 'Intel 1155',
                                'Intel 1156', 'Intel 2011', 'Intel 2011 v3',
                                'Intel 2066', 'Intel 1151', 'Intel 1151 v2',
                                'Intel 1200'], '148', '85')),
    (pc.Cooler('PCCooler GI-X3',
               'https://www.e-katalog.ru/jpg/1412947.jpg',
               'https://www.e-katalog.ru/PCCOOLER-GI-X3.htm',
               '1010', '2254', ['AMD AM4', 'AMD AM2', 'AMD AM3', 'AMD FM1',
                                'AMD FM2', 'Intel 1150', 'Intel 1155',
                                'Intel 1156', 'Intel 2011', 'Intel 2011 v3',
                                'Intel 1151', 'Intel 1151 v2',
                                'Intel 1200'], '154', ''))
]

# Вентеляторы
fans = [
    (pc.Fan('Cooler Master SickleFlow 120 ARGB 3 IN 1',
            'https://www.e-katalog.ru/jpg/1860666.jpg',
            'https://www.e-katalog.ru/COOLER-MASTER-SICKLEFLOW-120-ARGB-3-IN-1.htm',
            '2470', '3130', '120', '4', count='3')),
    (pc.Fan('Noctua NF-S12B redux-1200',
            'https://www.e-katalog.ru/jpg/603410.jpg',
            'https://www.e-katalog.ru/NOCTUA-NF-S12B-REDUX-1200.htm',
            '1150', '1630', '120', '3')),
    (pc.Fan('ID-COOLING DF-12025-ARGB TRIO',
            'https://www.e-katalog.ru/jpg/1751156.jpg',
            'https://www.e-katalog.ru/ID-COOLING-DF-12025-ARGB-TRIO.htm',
            '2474', '3199', '120', '4', count='3')),
    (pc.Fan('Deepcool MF120 GT',
            'https://www.e-katalog.ru/jpg/1885660.jpg',
            'https://www.e-katalog.ru/DEEPCOOL-MF120-GT.htm',
            '2998', '6022', '120', '4')),
    (pc.Fan('Noctua NF-A12X25 PWM',
            'https://www.e-katalog.ru/jpg/1584376.jpg',
            'https://www.e-katalog.ru/NOCTUA-NF-A12X25-PWM.htm',
            '2630', '2800', '120', '4', count='3'))
]