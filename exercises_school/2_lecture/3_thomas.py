from math import sqrt

def thomsons_formula():
    try:
        L = input("Zadej indukcnost [H]:")
        C = input("Zadej kapacitu [F]:")
        L = float(L)
        C = float(C)
        F = 1 / (2 * 3.14 * sqrt(L * C))
        return "Frekvence je: " + str(F) + "Hz"
    except ValueError:
        print("Zadana hodnota neni ciselna")

print(thomsons_formula())