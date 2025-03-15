from Book import Libro

class FastLibrary:
    def __init__(self):
        self.libri_perTitolo = {}
        self.libri_perAutore = {}

    def visualizza(self):
        if not self.libri_perTitolo: 
            print("FastLibreria vuota\n")
        else:
            for libro in self.libri_perTitolo.values():
                print(libro)

    def aggiungi(self,libro):
        self.libri_perTitolo[libro.titolo] = libro

        if libro.autore in self.libri_perAutore:
            self.libri_perAutore[libro.autore].append(libro)
        else:
            self.libri_perAutore[libro.autore] = libro

    def cerca_perTitolo(self,titolo):
        return self.libri_perTitolo.get(titolo, "Nessun libro trovato")
    
    def cerca_perAutore(self,autore):
        return self.libri_perAutore.get(autore, "Nessun libro trovato")
    
