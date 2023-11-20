class Auto:
    """ Trida auto reprezentuje auto pro simulaci realneho vozidlo pro cviceni PV na SPSE Jecna """

    def __init__(self, objem_nadrze_l : float, spotreba_na_100_km_l : float):
        """
        Konstruktor nastavi objem nadrze a spotrebu dle parametru a nastavi prazdnou nadrz.

        :param objem_nadrze_l: Objem nadrze v litrech
        :param spotreba_na_100_km_l: Spotreba na 100km v litrech
        """

        if (objem_nadrze_l < 0):
            raise Exception("Nadrz musi mit kladny objem")
        if (spotreba_na_100_km_l < 0):
            raise Exception("Spotreba nesmi byt zaporna")

        self.objem_nadrze_l = objem_nadrze_l
        self.spotreba_na_100_km_l = spotreba_na_100_km_l
        self._aktualni_objem_paliva_v_nadrzi_l = 0
        self._najeto_km = 0

    def aktualni_stav_nadrze(self) -> float:
        """
        Metoda vrati aktualni stav nadrze

        :return: Zbyle palivo v nadrzi v litrech
        """
        return self._aktualni_objem_paliva_v_nadrzi_l

    def aktualni_najeto_km(self) -> float:
        """
        Metoda vrati aktualni stav najetych km

        :return: Najete km
        """
        return self._najeto_km

    def natankuj(self, objem_l : float ) -> None:
        """
        Metoda natankuje auto o zadanou hodnotu
        :param objem_l:
        :return: None
        """
        if(objem_l < 0):
            raise Exception("Nelze odcerpat palivo pomoci metody natankovat")

        if((self._aktualni_objem_paliva_v_nadrzi_l + objem_l) > self.objem_nadrze_l):
            raise Exception("Nelze nacerpat vice nez je kapacita nadrze")

        self._aktualni_objem_paliva_v_nadrzi_l += objem_l

    def popojed(self, pocet_km : float ) -> None:
        """
        Metoda popojede auto o zadanou hodnotu, snizi stav paliva v nadrzi a zvysi pocet najetych km
        :param pocet_km:
        :return: None
        """
        if(pocet_km < 0):
            raise Exception("Couvani je take jizda, smer neresime")

        spotreba_paliva_l = pocet_km/100.0 * self.spotreba_na_100_km_l

        if(self._aktualni_objem_paliva_v_nadrzi_l < spotreba_paliva_l):
            raise Exception("Na jizdu neni dostatek paliva")

        self._aktualni_objem_paliva_v_nadrzi_l -= spotreba_paliva_l
        self._najeto_km += pocet_km


try:
    auto = Auto(30, 12.5)
    auto.objem_nadrze_l = 22.5
    auto.natankuj(2.5)
    auto.popojed(20)
except Exception as e:
    print(e)
    exit(1)