class HumanPlayer:
    def __init__(self):
        self
    
    def HumanPlay(self,to_guess):
        choice = int(input("Indovina il numero: "))

    
        while(1):
            if choice > to_guess:
                print("La tua scelta è troppo alta")
                choice = int(input("Indovina il numero: "))
            elif choice < to_guess:
                print("La tua scelta è troppo piccola")
                choice = int(input("Indovina il numero: "))
            else:
                print(f"Esatto, il numero è: {choice}")
                break