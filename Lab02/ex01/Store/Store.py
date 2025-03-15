from Store_Inventory import StoreInventory

class Store:
    def __init__(self,money, name, StoreInventory):
        self.money = money
        self.name = name
        self.StoreInventory = StoreInventory
    
    def __str__(self):
        return f"Il negozio {self.name} ha {self.money}€"
