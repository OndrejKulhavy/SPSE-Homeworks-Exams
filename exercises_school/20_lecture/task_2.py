import numpy as np


algoritmy = np.array(["Brute force", "Monte carlo", "Heuristika"])

casova_slozitost = np.array([
    [0.123, 0.456, 0.789],
    [0.22, 0.21, 0.22],
    [0.2, 0.342, 0.44],
])

pametova_slozitost = np.array([
    [1024, 2048, 4096],
    [2048, 4096, 8192],
    [4096, 8192, 16384],
])

pocet_prvku = np.array([3, 3, 3])

for i in range(len(algoritmy)):
    print(f"{algoritmy[i]}, časová složitost [sec]:", casova_slozitost[i])
    print(f"{algoritmy[i]}, paměťová složitost [B]:", pametova_slozitost[i])
    print(f"{algoritmy[i]}, počet prvků:", pocet_prvku[i], "\n")
