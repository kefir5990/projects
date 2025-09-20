import pandas as pd
from models.bike import Bike

class BikeDataset:
    def __init__(self, filepath):
        self.df = pd.read_csv(filepath)
        self.bikes = self._create_bikes()

    def _create_bikes(self):
        bikes = []
        for _, row in self.df.iterrows():
            bike = Bike(
                row['Brand'], row['Model'], row['Year'],
                row['KM_Driven'], row['Selling_Price'], row['Owner'],
                row['Seller_Type'], row.get('Ex_Showroom_Price')
            )
            bikes.append(bike)
        return bikes
