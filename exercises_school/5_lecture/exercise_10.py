class Zbozi:
    def __new__(cls, nazev, cena: float):
        if not nazev:
            instance = None
        elif cena < 0:
            instance = None
        else:
            instance = super().__new__(cls)

        return instance

    def __init__(self, nazev, cena):
        self.nazev = nazev
        self.cena = cena


a = Zbozi("Rohlik", 5)
b = Zbozi("Hackers item", -10)

print(a)
print(b)