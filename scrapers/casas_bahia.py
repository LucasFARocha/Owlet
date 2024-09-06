# CASAS BAHIA ESTÁ INCOMPLETA

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


def scrape_amazon(search):

    # Definindo a url da loja
    store_url = 'https://www.casasbahia.com.br/'

    # Definindo a url da pesquisa
    url = store_url + search.replace(' ', '-') + '/b'

    # Vai até a url designada
    driver.get(url)

    product_list = []  # Lista que será usada para armazenar os objetos

    # Encontra todos os elementos da Classe: "" no site (os cards de produtos)
    all_cards = driver.find_elements(By.CLASS_NAME, '')

    for product_card in all_cards:

        # O único que possui o atributo id é a barra de filtro de preços
        if product_card.get_attribute('id'):
            continue

        # ===== ÁREA DE PESQUISA DO PREÇO PROMOCIONAL =====
        # Fora do try geral porque não é obrigatório para o produto

        try:
            # Tente achar a tag que contém tanto o preço "riscado" quanto o preço da parcela
            search_prev_price = product_card.find_element(By.CLASS_NAME, '')

            # A tag que contém o preço da parcela NÃO possui esse atributo, ou seja,
            # ele verifica se é o preço "riscado" (preço original do produto em oferta)
            if search_prev_price.get_attribute(''):
                prev_price = float(search_prev_price.text[2:].replace('.', '').replace(',', '.'))
            else:
                prev_price = None

        except NoSuchElementException:
            prev_price = None

        # =================================================

        try:
            # Procurando a imagem
            search_image = product_card.find_element(By.CLASS_NAME, '')
            image = None

            # Pegando a imagem do produto, caso tenha o atributo srcset
            if search_image.get_attribute('srcset'):
                image = search_image.get_attribute('src')

            # Procurando a descrição
            search_description = product_card.find_element(By.CLASS_NAME, '')
            # Pegando a Descrição do Produto
            description = search_description.text

            search_link = product_card.find_element(By.CLASS_NAME, '')
            link = search_link.get_attribute('href')

            # Tente achar o preço
            search_price = product_card.find_element(By.CLASS_NAME, '')
            # Pegando o Preço do produto e colocando no formato do Banco
            price = float(search_price.text.replace('.', '').replace(',', '.'))

            # Tente achar a avaliação
            search_rating = product_card.find_element(By.CLASS_NAME, '')
            # Pegando a Avaliação do Produto e colocando no formato do Banco
            rating = float(search_rating.get_property('innerText').split(' ', 1)[0].replace(',', '.'))

        except NoSuchElementException:
            continue

        product = Product(image, description, link, price, prev_price, rating)  # Instanciando o objeto Product
        product_list.append(product)  # Adicionando o objeto na lista
        # fim do for

    driver.close()  # Fecha o navegador
    return product_list  # Retornando a lista com todos os objetos (produtos)
