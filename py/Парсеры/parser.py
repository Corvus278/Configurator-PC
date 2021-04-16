from selenium import webdriver


def main():
    driver = webdriver.Chrome()
    driver.get('https://www.e-katalog.ru/ek-list.php?katalog_=187&sb_=материнская+плата')

    all_links = driver.find_elements_by_tag_name('a')

    boards_links_url = []
    for link in all_links:
        if link.get_attribute('data-text') == 'ВЫ ИСКАЛИ':
            url = link.get_attribute('href')
            boards_links_url.append(url)

    print(boards_links_url)


if __name__ == '__main__':
    main()
