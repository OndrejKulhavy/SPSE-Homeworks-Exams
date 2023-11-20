import math


def calculate_circle_content(radius):
    if radius <= 0:
        raise ArithmeticError
    else:
        return radius * radius * math.pi


try:
    radius = input("Zadej polomer kruhu v cm: ")
    radius = int(radius)
    content = calculate_circle_content(radius)
    print(content)
except ValueError:
    print("Nejedna se o cislo. Nejsem schopny vypocitat obsah!")
except ArithmeticError:
    print("Hodnota polomeru nemuze byt <= 0")
