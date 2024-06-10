class Product:
    image = ''
    description = ''
    link = ''
    price = 0.0  # Preço do produto
    salePrice = 0.0  # Preço anterior do produto, caso seja uma promoção
    rating = 0.0

    def __init__(self, image, description, link, price, rating):
        self.image = image
        self.description = description
        self.link = link
        self.price = price
        self.rating = rating

    # def set_product(self, image, description, price, rating):
    #     self.image = image
    #     self.description = description
    #     self.price = price
    #     self.rating = rating

    # def set_image(self, image):
    #     self.image = image
    #
    # def set_description(self, description):
    #     self.description = description
    #
    # def set_price(self, price):
    #     self.price = price
        
    def set_sale_price(self, salePrice):
        self.salePrice = salePrice
    #
    # def set_rating(self, rating):
    #     self.rating = rating
