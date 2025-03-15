class Custumer:
    def __init__(self,name,type,discount):
        self.type = type
        self.discount = discount
        self.name = name

    def __str__(self):
        return f"Il cliente {self.name} di tipo {self.type} ha {self.discount}\n"
