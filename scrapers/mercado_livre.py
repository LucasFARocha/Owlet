from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException

from product import Product

# A classe Service é usada para iniciar uma instância do Browser WebDriver
service = Service()
# webdriver.FirefoxOptions é usado para definir a preferência para o browser do Firefox
options = webdriver.FirefoxOptions()

driver = webdriver.Firefox(service=service, options=options)  # Inicia-se a instãncia


def scrape_mercado_livre(search):
    # Definindo a url da loja
    store_url = 'https://lista.mercadolivre.com.br/'

    # Definindo a url da pesquisa
    url = store_url + search.replace(' ', '-')

    # Vai até a url designada, da Amazon
    driver.get(url)

    product_list = []  # Lista que será usada para armazenar os objetos

    # Encontra todos os elementos da Classe: "ui-search-result__wrapper" no site (os cards de produtos)
    all_cards = driver.find_elements(By.CLASS_NAME, 'ui-search-result__wrapper')

    for product_card in all_cards:

        # ===== ÁREA DE PESQUISA DO PREÇO PROMOCIONAL =====
        # Fora do try geral porque não é obrigatório para o produto

        try:
            # Tente achar a tag que contém o preço "riscado"
            search_prev_price = product_card.find_element(By.CLASS_NAME, 'ui-search-price__original-value')

            # Formatando o preço
            prev_price = float(search_prev_price.get_attribute('textContent')[2:].replace('.', '').replace(',', '.'))

        except NoSuchElementException:
            prev_price = None

        # =================================================

        try:
            # Procurando a imagem
            search_image = product_card.find_element(By.CLASS_NAME, 'ui-search-result-image__element')
            # Pegando a imagem do produto
            image = search_image.get_attribute('currentSrc')

            # Procurando a descrição
            search_description = product_card.find_element(By.CLASS_NAME, 'ui-search-item__title')
            # Pegando a Descrição do Produto
            description = search_description.text

            search_link = product_card.find_element(By.CLASS_NAME, 'ui-search-link__title-card')
            link = search_link.get_attribute('href')

            # Tente achar o preço
            search_price = product_card.find_element(By.CLASS_NAME,
                                                     'andes-money-amount.ui-search-price__part.ui-search-price__part--medium.andes-money-amount--cents-superscript')
            # Pegando o Preço do produto e colocando no formato do Banco
            price = float(search_price.get_attribute('textContent')[2:].replace('.', '').replace(',', '.'))

            # Tente achar a avaliação
            search_rating = product_card.find_element(By.CLASS_NAME, 'ui-search-reviews__rating-number')
            # Pegando a Avaliação do Produto e colocando no formato do Banco
            rating = float(search_rating.text)

        except NoSuchElementException:
            continue

        product = Product(image, description, link, price, prev_price, rating)  # Instanciando o objeto Product
        product_list.append(product)  # Adicionando o objeto na lista
        # fim do for

    driver.close()  # Fecha o navegador
    return product_list  # Retornando a lista com todos os objetos (produtos)