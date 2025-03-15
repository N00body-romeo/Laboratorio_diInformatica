from Book import Libro

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