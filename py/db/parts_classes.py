class Motherboard:
    def __init__(self, name, img, url, price_min, price_max, form, socket,
                 proc_list, pins, m2_count, m2_interface,
                 sata_count, fan_connector_count, ddr,
                 ram_frequency, ram_gb_count, ram_count,
                 ram_form='DIMM'):
        self.name = name
        self.img = img
        self.url = url
        self.price_min = price_min
        self.price_max = price_max
        self.form = form
        self.chipset = chipset
        self.proc_list = proc_list
        self.pins = pins
        self.m2_count = m2_count
        self.m2_interface = m2_interface
        self.stata_count = sata_count
        # self.fan_connector_type = fan_connector_type
        self.fan_connector_count = fan_connector_count
        self.ram_form = ram_form
        self.ddr = ddr
        self.ram_frequency = ram_frequency
        self.ram_gb_count = ram_gb_count
        self.ram_count = ram_count


class CPU:
    def __init__(self, name, img, url, price_min, price_max, socket, line,
                 generation):
        self.name = name
        self.img = img
        self.url = url
        self.price_min = price_min
        self.price_max = price_max
        self.socket = socket
        self.line = line
        self.generation = generation


class GPU:
    def __init__(self, name, img, url, price_min, price_max, slot, pins,
                 length):
        self.name = name
        self.img = img
        self.url = url
        self.price_min = price_min
        self.price_max = price_max
        self.slot = slot
        self.pins = pins
        self.length = length


class PowerSupply:
    def __init__(self, name, img, url, price_min, price_max, form,
                 connectors_pci_e_8__count, connectors_sata_count):
        self.name = name
        self.img = img
        self.url = url
        self.price_min = price_min
        self.price_max = price_max
        self.form = form
        self.connectors_pci_e_8__count = connectors_pci_e_8__count
        self.connectors_sata_count = connectors_sata_count


class Case:
    def __init__(self, name, img, url, price_min, price_max, form_motherboard,
                 power_supply, form__power_supply,
                 gpu_length_max, sata__2_5__count, sata__3_5__count, fans_front,
                 fans_top, fans_back):
        self.name = name
        self.img = img
        self.url = url
        self.price_min = price_min
        self.price_max = price_max
        self.form_motherboard = form_motherboard
        self.power_supply = power_supply
        self.form__power_supply = form__power_supply
        self.gpu_length_max = gpu_length_max
        self.sata__2_5__count = sata__2_5__count
        self.sata__3_5__count = sata__3_5__count
        self.fans_front = fans_front
        self.fans_top = fans_top
        self.fans_back = fans_back


class Storage:
    def __init__(self, name, img, url, price_min, price_max, form, sata_form='',
                 m2_form=''):
        self.name = name
        self.img = img
        self.url = url
        self.price_min = price_min
        self.price_max = price_max
        self.form = form
        self.sata_form = sata_form
        self.m2_form = m2_form

class RAM:
    def __init__(self, name, img, url, price_min, price_max, die_count, ddr,
                 all_volume, frequency, form='DIMM'):
        self.name = name
        self.img = img
        self.url = url
        self.price_min = price_min
        self.price_max = price_max
        self.die_count = die_count
        self.ddr = ddr
        self.all_volume = all_volume
        self.frequency = frequency
        self.form = form


class Cooler:
    def __init__(self, name, img, url, price_min, price_max, sockets, height,
                 width):
        self.name = name
        self.img = img
        self.url = url
        self.price_min = price_min
        self.price_max = price_max
        self.sockets = sockets
        self.height = height
        self.width = width


class WCS:
    def __init__(self, name, img, url, price_min, price_max, sockets):
        self.name = name
        self.img = img
        self.url = url
        self.price_min = price_min
        self.price_max = price_max
        self.sockets = sockets


class Fan:
    def __init__(self, name, img, url, price_min, price_max, weight, count='1'):
        self.name = name
        self.img = img
        self.url = url
        self.price_min = price_min
        self.price_max = price_max
        self.weight = weight
        self.count = count
