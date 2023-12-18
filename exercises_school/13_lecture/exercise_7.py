"""
Vytvorte ukazku kodu pro nasledujici priklady, ktere demonstruji pouziti uvedenych funkci pro praci se soubory:

Zjisteni jestli slozka existuje pomoci funkce path.isdir() z modulu os
Vytvoreni slozky pomoci funkce mkdir() v modulu os
Smazani prazdne slozky funkci rmdir() z modulu os
Smazani slozky vcetne obsahu funkci rmtree() z modulu shutil
Vypis obsahu slozky pomoci listdir() z modulu os
Vypis obsahu slozky a vsech jejich podslozek (kompletni prohledani vsech podslozek i jejich podslozek) libovolnym zpusobem
"""

import os
import shutil


def existuje_slozka(cesta):
    return os.path.isdir(cesta)


def vytvor_slozku(cesta):
    os.mkdir(cesta)


def smaz_prazdnou_slozku(cesta):
    os.rmdir(cesta)


def smaz_slozku_vcetne_obsahu(cesta):
    shutil.rmtree(cesta)


def vypis_obsah_slozky(cesta):
    obsah = os.listdir(cesta)
    print(obsah)


def vypis_obsah_a_podslozky(cesta):
    for slozka, podslozky, soubory in os.walk(cesta):
        print(f"Složka: {slozka}")
        print(f"Podsložky: {podslozky}")
        print(f"Soubory: {soubory}")


if __name__ == "__main__":
    cesta = "example"
    if not existuje_slozka(cesta):
        vytvor_slozku(cesta)
    vypis_obsah_slozky(cesta)
    vypis_obsah_a_podslozky(cesta)
    smaz_prazdnou_slozku(cesta)
    if existuje_slozka(cesta):
        smaz_slozku_vcetne_obsahu(cesta)