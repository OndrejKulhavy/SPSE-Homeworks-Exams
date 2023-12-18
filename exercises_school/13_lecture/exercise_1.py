"""
Upravte následující kod, ktery otevre soubor, zapise do nej "hello world" a soubor zavre, tak aby

file = open("helloworld.txt", "w")
file.write("Now the file has more content!")
file.close()
1. po spusteni do souboru zapsal Vase jmeno.

2. po kazdem spusteni do souboru pridal dalsi radek s dalsim textem, napriklad "hello world".

3. misto metod open() a close() pouzival konstrukci with open(...) as file: bez pouziti close()
"""


def write_name(name):
    with open("helloworld.txt", "a") as file:
        file.write(f"Hello {name}!\n")


if __name__ == "__main__":
    name = input("Enter your name: ")
    write_name(name)
