import random
from HumanPlayer import HumanPlayer
from CpuPlayer import CpuPlayer

def main():

    range = int(input("Scegli un numero positivo: "))
    to_guess = random.randint(0, range)
    print(f"Risposta: {to_guess}")

    while(1):
        print('Giocatori disponibili: "Human" e "CPU", "x" per uscire')
        scelta = input("Chi gioca? ")
        if scelta == "Human":
            io = HumanPlayer()
            io.HumanPlay(to_guess)
            break;
        elif scelta == "CPU":
            cpu = CpuPlayer()
            cpu.CpuPlay(to_guess,range)
            break;
        elif scelta == "x":
            print("Uscita in corso...\n")
            break;
        else:
            print("Input non valido")


if __name__ == "__main__":
    main()
