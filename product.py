class Product:
    image = ''
    description = ''
    link = ''
    price = 0.0  # Preço do produto
    prev_price = 0.0  # Preço anterior do produto, caso seja uma promoção
    rating = 0.0

    def __init__(self, image, description, link, price, prev_price, rating):
        self.image = image
        self.description = description
        self.link = link
        self.price = price
        self.prev_price = prev_price
        self.rating = rating
