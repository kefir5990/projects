class Bike:
    def __init__(self, brand, model, year, km_driven, price, owner, seller_type, showroom_price):
        self.brand = brand
        self.model = model
        self.year = year
        self.km_driven = km_driven
        self.price = price
        self.owner = owner
        self.seller_type = seller_type
        self.showroom_price = showroom_price

    def depreciation(self):
        if self.showroom_price and self.price:
            return self.showroom_price - self.price
        return None
