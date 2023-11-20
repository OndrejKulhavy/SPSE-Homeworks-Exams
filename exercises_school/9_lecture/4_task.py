"""
Opravte níže uvedenou metodu generatorSudychCisel(..) tak, aby správně generoval pouze sudá čísla:
"""


def generatorSudychCisel(od, do):
    i = od
    while i < do:
        if i % 2 == 0:
            yield i
        i = i+1


if __name__ == "__main__":
    print("Suda cisla")
    for x in generatorSudychCisel(1, 50):
        print(x)
