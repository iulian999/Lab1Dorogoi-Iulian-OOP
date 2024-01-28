class Carte:
    def __init__(self, titlu, autor, isbn):
        self.titlu = titlu
        self.autor = autor
        self.isbn = isbn

    def __str__(self):
        return f"{self.titlu} - {self.autor} ({self.isbn})"

class Biblioteca:
    def __init__(self):
        self.carti = []

    def adauga_carte(self, carte):
        self.carti.append(carte)
        print(f"Cartea '{carte.titlu}' a fost adăugată în bibliotecă.")

    def elimina_carte(self, isbn):
        for carte in self.carti:
            if carte.isbn == isbn:
                self.carti.remove(carte)
                print(f"Cartea '{carte.titlu}' a fost eliminată din bibliotecă.")
                return
        print("Cartea cu ISBN-ul specificat nu a fost găsită în bibliotecă.")

    def afiseaza_carti(self):
        if not self.carti:
            print("Biblioteca este goală.")
        else:
            print("Cărți în bibliotecă:")
            for carte in self.carti:
                print(carte)

if __name__ == "__main__":
    biblioteca = Biblioteca()

    while True:
        print("\n 1. Adaugă carte")
        print("\n 2. Elimină carte")
        print("\n 3. Afișează cărți")
        print("\n 0. Ieșire")

        optiune = input("\n Selectați o opțiune: ")

        if optiune == "1":
            titlu = input("Introduceți titlul cărții: ")
            autor = input("Introduceți autorul cărții: ")
            isbn = input("Introduceți ISBN-ul cărții: ")
            carte = Carte(titlu, autor, isbn)
            biblioteca.adauga_carte(carte)

        elif optiune == "2":
            isbn = input("Introduceți ISBN-ul cărții de eliminat: ")
            biblioteca.elimina_carte(isbn)

        elif optiune == "3":
            biblioteca.afiseaza_carti()

        elif optiune == "0":
            print("Programul s-a încheiat.")
            break
        
        else:
            print("Opțiune invalidă. Încercați din nou.")