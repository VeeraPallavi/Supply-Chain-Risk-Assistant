import pandas as pd

class DataLoader:
    def __init__(self, orders_path, inventory_path):
        self.orders_path = orders_path
        self.inventory_path = inventory_path
    

    def load_orders(self):
        orders_df = pd.read_csv(self.orders_path)

        orders_df["delivery_time_days"]= (orders_df["delivery_time_days"].fillna(0))
        orders_df["status"] = (orders_df["status"].fillna("Unknown"))

        return orders_df
    
    def load_inventory(self):
        inventory_df = pd.read_csv(self.inventory_path)

        inventory_df["stock_level"] = (inventory_df["stock_level"].fillna(-1))
        inventory_df["transport_cost"] = (inventory_df["transport_cost"].fillna(-1))

        return inventory_df

    