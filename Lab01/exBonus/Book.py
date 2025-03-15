class Libro:
    def __init__(self,titolo, autore, anno, genere):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.genere = genere

    def __str__(self):
        return f"Titolo: {self.titolo}, Autore: {self.autore}, Anno: {self.anno}, Genere: {self.genere}"
