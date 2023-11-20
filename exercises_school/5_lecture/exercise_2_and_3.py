class ZamceneDvereException(Exception):
    """
    Výjimka reprezentující pokus o otevření zamčených dveří.

    Použití:
    try:
        d.otevrit()
    except ZamceneDvereException as e:
        print("Dvere jsou zamcene, nemuzes je otevrit")
    """

class Dvere:
    """
    Třída reprezentující dveře.

    Atributy:
    - zamceno (bool): True, pokud jsou dveře zamčené, jinak False.
    - otevreno (bool): True, pokud jsou dveře otevřené, jinak False.

    Metody:
    - __init__(self, zamceno: bool): Inicializuje objekt Dvere s daným stavem zamčenosti.
    - otevrit(self): Otevře dveře, pokud nejsou zamčené.
    - zavrit(self): Zavře dveře.
    - zamknout(self): Zamkne dveře, pokud nejsou otevřené.
    - odemknout(self): Odemkne dveře.
    """
    def __init__(self, zamceno: bool):
        self.zamceno = zamceno
        self.otevreno = False
    def otevrit(self):
        """
        Otevře dveře, pokud nejsou zamčené.
        Pokud jsou zamčené, vyvolá výjimku ZamceneDvereException.
        """
        if self.zamceno:
            raise ZamceneDvereException()
        self.otevreno = True

    def zavrit(self):
        """
        Zavře dveře.
        """
        self.otevreno = False

    def zamknout(self):
        """
        Zamkne dveře, pokud nejsou otevřené.
        Pokud jsou otevřené, vyvolá ValueError.
        """
        if self.otevreno:
            raise ValueError("Nelze zamknout otevrene dvere")
        self.zamceno = True

    def odemknout(self):
        """
        Odemkne dveře.
        """
        self.zamceno = False


d = Dvere(zamceno=True)
try:
    d.otevrit()
    print("Prosel jsem")
except ZamceneDvereException as e:
    print("Dvere jsou zamcene, nemuzes je otevrit")
    print("Neprošel jsem")