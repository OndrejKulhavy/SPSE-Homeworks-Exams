"""
Vytvořte program, který v případě, že běží neumožní další spuštění, tedy půjde zapnout jen jednou.

K tomuto řešení se použijte souborový zámek podle následujícícho algoritmu:

Program na začátku otevře soubor s názvem lock.dat v binárním módu a načte jeden první byte.
Pokud je první byte roven hodnotě b'0x00' tak program do tohoto souboru jako první byte zapíše hodnotu b'0xFF' můžete běžet.
 Po skončení práce opět zapíše do souboru byte b'0x00'. (pro otestování můžete zkusit příkaz sleep z modulu time, který bude simulovat běh programu)
Pokud soubor nebude existovat program ho nejprve vytvoří a defaultně zapíše b'0x00'
Pokud soubor bude existovat a bude v něm hodnota jiná hodnota než b'0x00', tak se program ukončí na napíše uživateli, že již běží jiná instance programu.
"""

import os
import time


def lock():
    if os.path.exists("lock.dat"):
        with open("lock.dat", "rb") as file:
            if file.read(1) == b"\x00":
                with open("lock.dat", "wb") as file:
                    file.write(b"\xFF")
                return True
            else:
                return False
    else:
        with open("lock.dat", "wb") as file:
            file.write(b"\xFF")
        return True


def unlock():
    with open("lock.dat", "wb") as file:
        file.write(b"\x00")


if __name__ == "__main__":
    if not lock():
        print("Program is already running.")
        exit(1)

    print("Program is running.")
    time.sleep(10)
    print("Program finished.")
    unlock()
