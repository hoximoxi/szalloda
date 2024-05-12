from datetime import datetime

class Szoba:
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(ar=5000, szobaszam=szobaszam)

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(ar=8000, szobaszam=szobaszam)

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

class Foglalás:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

    def get_ar(self):
        return self.szoba.ar

class FelhasznaloiInterface:
    def __init__(self, szalloda):
        self.szalloda = szalloda
        self.foglalasok = []

    def foglalas(self, szobaszam, datum):
        today = datetime.now().date()
        if datum.date() < today:
            print("A foglalás érvénytelen, mert múltbéli dátumra történt.")
            return
        
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum.date():
                print("A szoba már foglalt ekkor.")
                return
        for szoba in self.szalloda.szobak:
            if szoba.szobaszam == szobaszam:
                foglalas = Foglalás(szoba, datum.date())
                self.foglalasok.append(foglalas)
                print(f"Sikeres foglalás a {datum.date()} dátumra a(z) {szobaszam} szobára.")
                return
        print("Nincs ilyen szoba.")

    def lemondas(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                print(f"Sikeres lemondás a {datum} dátumra a(z) {szobaszam} szobára.")
                return
        print("Nincs ilyen foglalás.")

    def listaz(self):
        if not self.foglalasok:
            print("Jelenleg nincs foglalás.")
        else:
            print("Foglalások:")
            for foglalas in self.foglalasok:
                print(f"{foglalas.szoba.szobaszam} szoba, {foglalas.datum}")

if __name__ == "__main__":
    # Szálloda létrehozása
    szalloda = Szalloda("Celestial Palace")

    # Szobák hozzáadása a szállodához
    egyagyas_szoba1 = EgyagyasSzoba("101")
    ketagyas_szoba1 = KetagyasSzoba("201")
    ketagyas_szoba2 = KetagyasSzoba("202")

    szalloda.add_szoba(egyagyas_szoba1)
    szalloda.add_szoba(ketagyas_szoba1)
    szalloda.add_szoba(ketagyas_szoba2)

    # Felhasználói interfész inicializálása
    felhasznaloi_interfesz = FelhasznaloiInterface(szalloda)
    
    while True:
        print("Üdvözöljük a Celestial Palace-ban")
        print("\n1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("4. Kilépés")

        valasztas = input("Válasszon egy műveletet: ")

        if valasztas == "1":
            szobaszam = input("Adja meg a foglalandó szoba számát: ")
            datum_str = input("Adja meg a foglalás dátumát (ÉÉÉÉ-HH-NN formátumban): ")
            datum = datetime.strptime(datum_str, "%Y-%m-%d")
            felhasznaloi_interfesz.foglalas(szobaszam, datum)
        elif valasztas == "2":
            szobaszam = input("Adja meg a lemondandó foglalás szoba számát: ")
            datum_str = input("Adja meg a lemondandó foglalás dátumát (ÉÉÉÉ-HH-NN formátumban): ")
            datum = datetime.strptime(datum_str, "%Y-%m-%d")
            felhasznaloi_interfesz.lemondas(szobaszam, datum)
        elif valasztas == "3":
            felhasznaloi_interfesz.listaz()
        elif valasztas == "4":
            break
        else:
            print("Érvénytelen választás. Kérem válasszon egy számot a menüből!")