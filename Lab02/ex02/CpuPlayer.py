import random

def CpuPlay_AUX(to_guess, pivot, min_N, max_N):
    if pivot < to_guess:
        print(f"Numero scelto {pivot} è troppo piccolo.")
        min_N = pivot + 1
    elif pivot > to_guess:
        print(f"Numero scelto {pivot} è troppo grande.")
        max_N = pivot - 1
    else:
        print(f"CPU ha indovinato! Risposta = {pivot}")
        return pivot, min_N, max_N  #fine

    return pivot, min_N, max_N  #continua la ricerca

class CpuPlayer:
    def __init__(self):
        pass

    def CpuPlay(self, to_guess, N):
        min_N = 0
        max_N = N
        choice = (min_N + max_N) // 2  #prima scelta è pivot

        while True:
            choice, min_N, max_N = CpuPlay_AUX(to_guess, choice, min_N, max_N)

            if choice == to_guess:
                break

            choice = (min_N + max_N) // 2
