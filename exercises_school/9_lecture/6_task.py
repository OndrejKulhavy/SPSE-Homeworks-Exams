""""
Upravte následující zdrojový  kód:
Aby vypisoval stejné hodnoty i v případě, že vlastnost se jménem jezera bude definována takto:
"""


class KarsLakesGenerator():
    i = 0
    j = 0

    lakes = [
        ["Dyje", ["Křivé jezero", "Květné jezero", "Kutnar", "Mahenovo jezero"]],
        ["Labe", ["Babinecká tůň", "Hrbáčkovy tůně"]],
        ["Bílina", ["Komořanské jezero"]],
        ["(bez řeky)",
        ["Antošovické jezero", "Holásecká jezera", "Krňák", "Kurfürstovo rameno", "Malá říčka", "Podhradská tůň"]]
    ]

    def __iter__(self):
        self.i = 0
        self.j = 0
        return self

    def __next__(self):
        if self.i > (len(self.lakes) - 1):
            raise StopIteration()

        river = self.lakes[self.i][0]
        is_on_river = self.lakes[self.i][1]

        if self.j > (len(is_on_river) - 1):
            self.j = 0
            self.i = self.i + 1

        tmp = is_on_river[self.j]
        if river != "(bez řeky)":
            tmp += " (" + river + ")"
        self.j = self.j + 1
        return tmp


if __name__ == "__main__":
    for lake in KarsLakesGenerator():
        print(lake)
