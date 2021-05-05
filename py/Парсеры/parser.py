from selenium import webdriver
from icecream import ic
import time


class Motherboard:
    def __init__(self, name, img, form, chipset, proc_list, pins, m2_count, m2_interface, sata_count,
                 fan_connector_type, fan_connector_count, ddr, ram_frequency, ram_gb_count, ram_count, ram_form='DIMM'):
        self.name = name
        self.img = img
        self.form = form
        self.chipset = chipset
        self.proc_list = proc_list
        self.pins = pins
        self.m2_count = m2_count
        self.m2_interface = m2_interface
        self.stata_count = sata_count
        self.fan_connector_type = fan_connector_type
        self.fan_connector_count = fan_connector_count
        self.ram_form = ram_form
        self.ddr = ddr
        self.ram_frequency = ram_frequency
        self.ram_gb_count = ram_gb_count
        self.ram_count = ram_count


def pars_matherboard_spec(all_board_spec):
    for board_spec in all_board_spec:
        form_flag = True    # Слово "форм-фактор" используется два раза в характеристиках
        for spec in board_spec:
            # Форм-фактор
            if 'Форм-фактор' in spec and form_flag:
                form_factor = spec[len('Форм-фактор'):]
                form_flag = False
            # Чипсет
            elif 'Чипсет' in spec and len(spec) > len('Чипсет'):
                chipset = spec[len('Чипсет'):]
            # RAM - DDR и кол-во
            elif 'DDR' in spec:
                ram_ddr = spec[:len('DDR')]
                ram_count = spec[len('DDR')+2]
            # RAM - форм-фактор
            elif 'Форм-фактор' in spec and not(form_flag):
                form_ram = spec[len('Форм-фактор слота для памяти'):]
            # RAM - frequency
            elif 'Максимальная тактовая частота' in spec:
                ram_frequency = spec[len('Максимальная тактовая частота '):-4]
            # RAM max GB
            elif 'Максимальный объем памяти' in spec:
                ram_gb_count = spec[len('Максимальный объем памяти '):-3]
            # SATA count
            elif 'SATA' in spec:
                sata_count = spec[-4:-3]
            # М2 count
            elif 'M.2 разъем' in spec:
                m2_count = spec[-4:-3]
            #

def main():
    start1 = time.time()
    start_link = 'https://www.e-katalog.ru/ek-list.php?katalog_=187&sb_=материнская+плата'

    # Для более быстрой загрузки отключаем загрузку картинок и некоторго css
    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_setting_values': {'images': 2,
                            'plugins': 2, 'popups': 2, 'geolocation': 2,
                            'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2,
                            'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                            'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2,
                            'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
                            'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2,
                            'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2,
                            'durable_storage': 2}}
    options.add_experimental_option('prefs', prefs)
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")

    # Запускаем браузер и переходим на превую страницу
    driver = webdriver.Chrome(options=options)
    driver.get(start_link)

    start = time.time()
    # Вытаскиваем все ссылки на продукт, название платы, добавляем в соответствующие списки
    boards_links_urls = []
    boards_names = []
    boards_links = driver.find_elements_by_xpath("//a[@data-text='ВЫ ИСКАЛИ']")
    # Добавляем в список ссылки
    for link in boards_links:
        url = link.get_attribute('href')
        boards_links_urls.append(url)
        # Берём из ссылок их текст, добавляем в список имён
        name = link.get_attribute('text')
        boards_names.append(name)

    # Переходим к продукту (в описание)
    # берём от туда фотографию платы, ссылку на характеристики, добавляем в списки
    specifications_link_urls = []
    boards_photos = []
    for board_link in boards_links_urls:
        driver.get(board_link)
        # Ссылка на характеристики
        link = driver.find_element_by_link_text('ХАРАКТЕРИСТИКИ')
        url = 'https://www.e-katalog.ru' + link.get_attribute('link')
        specifications_link_urls.append(url)
        # Сслылка на фото
        photo = driver.find_element_by_xpath("//img[@rel='v:photo']")
        boards_photos.append(photo.get_attribute('src'))
        # Название
        # Сперва удаляем из разметки блок с ценами, что бы избавится от лишних span-ов
        element = driver.find_element_by_class_name('desc-short-prices-div')
        driver.execute_script("""
        var element = arguments[0];
        element.parentNode.removeChild(element);
        """, element)
        spans = driver.find_elements_by_tag_name('span')
        board_name = spans[41].get_attribute('innerHTML')
        boards_names.append(board_name)

    # Находим две таблицы с характеристиками, забираем из них всё содержимое
    all_spec_list = []
    for spec_link in specifications_link_urls:
        spec_tbody = []
        driver.get(spec_link)
        all_tbody = driver.find_elements_by_tag_name('tbody')
        spec_tbody.append(all_tbody[5].text)
        spec_tbody.append(all_tbody[6].text)
        all_spec_list.append(spec_tbody)

    # Закрытие браузера
    driver.quit()

    """ Работа с браузером окончена, теперь работаем с полученными данными. """

    # with open('out.txt', 'w', encoding='utf-8') as f:
    #     for i in all_spec_list:
    #         for j in i:
    #             f.write(j)

    # Подсчёт времени, ушедшего на выполнение кода
    end = time.time()
    print(end - start)


if __name__ == '__main__':
    main()
