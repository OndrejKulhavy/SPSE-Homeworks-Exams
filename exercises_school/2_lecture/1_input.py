import math

# This function adds 1 to any number you put into it
def algorithm():
    try:
        x = input("Zadej cislo: ")
        y = int(x) + 1
        print(y)
    except ValueError:
        print("Nejedna se o cislo! Zkus to znovu")
        # Handling incorrect values
        algorithm()


algorithm()