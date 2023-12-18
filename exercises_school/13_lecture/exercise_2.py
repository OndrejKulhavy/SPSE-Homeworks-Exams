"""
Napiste program, ktery vypise na obrazovku obsah souboru z ulohy 12.1 nasledujicim zpusobem:

1. pomoci metody read() bez parametru vypiste cely soubor.

2. pomoci metody readline() vypiste jen prvni radek.

3. pomoci metody read( .. ) s parametrem vypiste jen prvni tri znaky.

4. pomoci cyklu forech na proměnné souboru (napr. for line file:) vypiste vsechny radky ocislovane, tedy cislo radku, mezera a obsah radku.
"""


def read(n: int = None) -> str:
    with open("helloworld.txt", "r") as file:
        if not n:
            return file.read()
        return file.read(n)


def readline() -> str:
    with open("helloworld.txt", "r") as file:
        return file.readline()


def read_numbred() -> str:
    with open("helloworld.txt", "r") as file:
        return "".join(f"{i} {line}" for i, line in enumerate(file))


if __name__ == "__main__":
    print(read())
    print(readline())
    print(read(3))
    print(read_numbred())
