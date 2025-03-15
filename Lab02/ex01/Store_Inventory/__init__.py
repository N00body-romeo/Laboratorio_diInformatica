class StoreInventory:
    def __init__(self,object,quantity):
        self.object = object
        self.quantity = quantity

    def Store_Inventory(self,object,quantity):
        store = {object:quantity}
        return store
