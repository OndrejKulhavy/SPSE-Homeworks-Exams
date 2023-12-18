"""
Predpokladejte nasledujici zdrojovy kod, kde nejprve otevreme soubor 2x, jednou pro zapis a jednou pro cteni, pak zapiseme data a nasledne je chceme precist. Nakonec soubory zavreme:

file_writer = open("text.txt", "w")
file_reader = open("text.txt", "r")

file_writer.write("Dneska prsi. \r\n")
file_writer.write("Zitra bude taky. \r\n")

print("1.radek: " + file_reader.readline())
print("2.radek: " + file_reader.readline())

file_writer.close()
file_reader.close()

Predpokladejme, ze soubory musi byt otevreny a zavreny zaroven - tedy nelze zmenit ze na prvnich dvou radcich je soubor 2x otevren a az na konci 2x zavren.

Vase ukoly jsou nasledujici:

1. Vysvetlete proc program nevypisuje obsah souboru

2. Zajistete doplnenim volani metody flush() mezi zapisem a ctenim, aby se vse co bylo do souboru zapsano skutecne zapsalo na disk.

3. Zajistete nastavenim bufferu v metode open(..) a atributu buffering, aby reseni z bodu 2. fungovalo i bez flush().
"""


def write_and_read():
    file_writer = open("text.txt", "w", buffering=1)
    file_reader = open("text.txt", "r")

    file_writer.write("Dneska prsi. \r\n")
    file_writer.write("Zitra bude taky. \r\n")

    print("1.radek: " + file_reader.readline())
    print("2.radek: " + file_reader.readline())

    file_writer.close()
    file_reader.close()


if __name__ == "__main__":
    write_and_read()
