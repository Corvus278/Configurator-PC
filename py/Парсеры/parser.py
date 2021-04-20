from selenium import webdriver
import time


def main():
    # Запускаем браузер
    start1 = time.time()
    start_link = 'https://www.e-katalog.ru/ek-list.php?katalog_=187&sb_=материнская+плата'
    driver = webdriver.Chrome()
    driver.get(start_link)

    start = time.time()
    # Вытаскиваем все ссылки из страницы
    all_links = driver.find_elements_by_tag_name('a')
    # Из всех ссылок берём те, которые ведут на продукт, и добавляем в список
    boards_links_urls = []
    for link in all_links:
        if link.get_attribute('data-text') == 'ВЫ ИСКАЛИ':
            url = link.get_attribute('href')
            boards_links_urls.append(url)

    # Переходим к продукту, и берём от туда ссылку на характеристики, добавляем в список
    specifications_link_urls = []
    for board_link in boards_links_urls:
        driver.get(board_link)
        all_links = driver.find_elements_by_tag_name('a')
        for link in all_links:
            if link.text == 'ХАРАКТЕРИСТИКИ':
                url = 'https://www.e-katalog.ru' + link.get_attribute('link')
                specifications_link_urls.append(url)
                break



    end = time.time()
    print(end - start)
    print(end - start1)


if __name__ == '__main__':
    main()

