class Item:
    def __init__(self,name,type,s_hand):
        self.type = type
        self.s_hand = s_hand
        self.name = name

    def __str__(self):
        f"L'oggetto {self.name} di tipo {self.type} {self.s_hand}"
