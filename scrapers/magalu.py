from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from product import Product

service = Service()
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service, options=options)


def scrape_magalu(search):
    store_url = 'https://www.magazineluiza.com.br/busca/'
    url = store_url + search.replace(' ', '+')

    # Vai até a url designada
    driver.get(url)

    # product_list = []  # Lista que será usada para armazenar os objetos
    product_list = []

    # Encontra todos os elementos da Classe: "sc-SSKRe.kzxbRz" no site (os cards de produtos)
    all_cards = driver.find_elements(By.CLASS_NAME, 'sc-SSKRe.kzxbRz')
    print('all_cards = driver.find_elements(By.CLASS_NAME, sc-SSKRe.kzxbRz)')

    for product_card in all_cards:
        print('for product_card in all_cards:')
        try:
            search_prev_price = product_card.find_element(By.CLASS_NAME, 'sc-kpDqfm.efxPhd.sc-gEkIjz.jmNQlo')
            prev_price = float(search_prev_price.text.split(' ', 1)[1].replace('.', '').replace(',', '.'))
        except NoSuchElementException:
            prev_price = None

        try:
            search_image = product_card.find_element(By.CLASS_NAME, 'sc-cWSHoV.iJPAvC')
            image = search_image.get_attribute('src')

            search_description = product_card.find_element(By.CLASS_NAME, 'sc-doohEh.dHamKz')
            description = search_description.text

            search_link = product_card.find_element(By.CLASS_NAME, 'sc-eBMEME.uPWog.sc-dxUMQK.jeUYOh.sc-dxUMQK.jeUYOh')
            link = search_link.get_attribute('href')

            search_price = product_card.find_element(By.CLASS_NAME, 'sc-kpDqfm.eCPtRw.sc-bOhtcR.dOwMgM')

            price = float(search_price.text.split(' ', 1)[1].replace('.', '').replace(',', '.'))

            search_rating = product_card.find_element(By.CLASS_NAME, 'sc-epqpcT.jdMYPv')
            rating = float(search_rating.text.split(' ', 1)[0])

            print('Encontrei :D')
        except NoSuchElementException:
            print('Não encontrei :/')
            continue

        product = Product(image, description, link, price, prev_price, rating)  # Instanciando o objeto Product
        product_list.append(product)  # Adicionando o objeto na lista

    driver.close()  # Fecha o navegador

    return product_list  # Retornando a lista com todos os objetos (produtos)
