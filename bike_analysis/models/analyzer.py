class Analyzer:
    def __init__(self, bikes):
        self.bikes = bikes

    def average_price_by_brand(self):
        brand_prices = {}
        brand_counts = {}
        for bike in self.bikes:
            if bike.brand and bike.price:
                brand_prices.setdefault(bike.brand, 0)
                brand_counts.setdefault(bike.brand, 0)
                brand_prices[bike.brand] += bike.price
                brand_counts[bike.brand] += 1
        return {brand: brand_prices[brand] / brand_counts[brand] for brand in brand_prices}
    
    def cheapest_bikes(self, top_n=5):
        return sorted(self.bikes, key=lambda b: b.price)[:top_n]

    def lowest_km_bikes(self, top_n=5):
        return sorted(self.bikes, key=lambda b: b.km_driven)[:top_n]
    
    def best_bikes_for_purchase(self, top_n=5):
        bikes = [b for b in self.bikes if b.price and b.km_driven]
        bikes.sort(key=lambda b: b.price + b.km_driven)
        return bikes[:top_n]
    
    def bikes_by_brand(self, brand_name):
        return [b for b in self.bikes if b.brand.lower() == brand_name.lower()]
