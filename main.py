from scrapers.amazon import scrape_amazon
# from scrapers.magalu import scrape_magalu

search = 'Smart Watch'
all_products = scrape_amazon(search)
# declarando all_products como uma lista que contém os valores retornados pela função

for product in all_products:
    # declarando product como um valor da lista, que nesse caso é um objeto

    print(product.image, product.description, product.link, product.price, product.prev_price, product.rating, sep=' - ')
