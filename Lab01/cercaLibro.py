# Crea un semplice programma per gestire una libreria di libri utilizzando la
# programmazione a oggetti in Python. Il programma deve consentire di aggiungere,
# visualizzare e cercare libri all'interno della libreria.

class Libro:
    def __init__(self,titolo, autore, anno, genere):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.genere = genere

    def toString(self):
        return f"Titolo: {self.titolo}, Autore: {self.autore}, Anno: {self.anno}, Genere: {self.genere}"
    

class Libreria:
    def __init__(self):
        self.libri = []
    
    def aggiungi(self,libro):
        self.libri.append(libro)

    def visualizza(self):
        if not self.libri: 
            print("Libreria vuota\n")
        else:
            for libro in self.libri:
                print(libro)

    def cerca_perTitolo(self, titolo):
        for libro in self.libri:
            if libro.titolo == titolo:
                return libro.toString()
        else: return "Nessun libro trovato per il seguente titolo"

    def cerca_perAnno(self,anno):
        lista = []
        for libro in self.libri:
            if libro.anno == anno:
                lista.append(libro.toString())
        
        if lista == []: return "Nessun libro trovato con questa data"
        for libro in lista:
            print(libro)
        

def main():

    book1 = Libro("1984","George Orwell", 1949, "Distopia")
    book2 = Libro("Commedia", "Dante Alighieri", 1500, "Romantico")
    book3 = Libro("La cacca è blu", "Grande Puffo", 2077, "Curioso")
    
    libreria = Libreria()
    libreria.aggiungi(book1)
    libreria.aggiungi(book2)
    libreria.aggiungi(book3)

    libreria.visualizza()

    while True:
        print("\n1. Aggiungi libro")
        print("\n2. Visualizza libri")
        print("\n3. Cerca libro per titolo")
        print("\n4. Cerca libro per anno")
        print("\n5. Esci")

        scelta = input("Scegli un'opzione: ")
 
        if scelta == '1':
            titolo = input("Inserisci il titolo del libro: ")
            autore = input("Inserisci l'autore del libro: ")
            anno = int(input("Inserisci l'anno di pubblicazione: "))
            genere = input("Inserisci il genere del libro: ")
            libro = Libro(titolo, autore, anno,genere)
            libreria.aggiungi(libro)
            print("Libro aggiunto con successo!")
        elif scelta == '2':
            libreria.visualizza()
        elif scelta == '3':
            titolo = input("Inserisci il titolo del libro da cercare: ")
            libro = libreria.cerca_perTitolo(titolo)
            print(libro)
        elif scelta == '4':
            anno = int(input("Inserisci l'anno del libro da cercare: "))
            libro = libreria.cerca_perAnno(anno)
            print(libro)
        elif scelta == '5':
            print("Uscita dal programma.")
            break
        else:
            print("Opzione non valida. Riprova.")

if __name__ == "__main__":
    main()
