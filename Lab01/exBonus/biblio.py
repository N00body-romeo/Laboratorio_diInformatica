# Bonus: creare una versione con le seguenti caratteristiche:
# 1) Le classi distribuite su file differenti (Book.py, Library.py, biblio.py, quest’ultimo
# come punto di accesso)
# 2) biblio.py creare una libreria di 100.000 libri generati automaticamente (ad es. con
# nomi random o con nomi tipo f“libro{num}” oppure “libro”+str(num) e num
# incrementale)
# 3) Efficiente dal punto di vista della ricerca dei libri (O(1) invece che O(n))
# 4) Calcolare il tempo richiesto da n ricerche di numeri casuali all’interno di questa
# libreria (con implementazione a dizionario) e di quella con implementazione a
# lista
# ● Nota: questo richiede di avere due classi, ad es. Library e FastLibrary, con una
# condivisione di metodi (per evitare la duplicazione di codice)


from Book import Libro
from Library import Libreria
from FastLibrary import FastLibrary

import random

def crea_Libreria(n):
    libreria = Libreria()
    generi = ["Fantasy", "Romantico", "Curioso", "Giallo", "Altro"]
    for i in range(1,n+1):
        titolo = f"Libro{i}"
        autore = f"Autore{i}"
        anno = random.randint(0,2025)
        genere = random.choice(generi)
        libro = Libro(titolo,autore,anno,genere)
        libreria.aggiungi(libro)
    return libreria

def crea_FastLibreria(n):
    libreria = FastLibrary()
    generi = ["Fantasy", "Romantico", "Curioso", "Giallo", "Altro"]
    for i in range(1,n+1):
        titolo = f"Libro{i}"
        autore = f"Autore{i}"
        anno = random.randint(0,2025)
        genere = random.choice(generi)
        libro = Libro(titolo,autore,anno,genere)
        libreria.aggiungi(libro)
    return libreria

def main():
    n = 100000
    Libreria = crea_Libreria(n)
    print("Libreria creato con successo")

    print("\\\\+++++++++++++++++++---------+++++++++++++++++++\\\\")

    FastLib = crea_FastLibreria(n)
    print("\nFastLibreria creato con successo")

# costo Libreria per ricerca: O(n)
# costo FastLibreria per ricerca: O(1) per titolo, O(1) per autore se unico, 
    # O(k) per k libri dello stesso autore



if __name__ == "__main__":
    main()