"""
Zopakujte si vestavěné funkce map(...), reduce(....), filter(...) z dokumentace https://docs.python.org/3/library/functions.html nebo z tutoriálu

Přehrát video
 a pomocí lambda definic vyřešte následující úlohy nad kolekcí:
pole = [100.10, 323.2, 355.9, 214.19, 87.0]
Vytvorte kombinaci funkci list(map(...)) a lambda vyrazu pole2, kde budou hodnoty vyssi o 30% z promenne pole
Vytvore kombinaci funkci list(filter(...)) a lambda vyrazu pole3, kde budou hodnoty vyssi nez 120.0 z promenne pole
Vytvorete kombinaci funkci list, filter a map a lamda vyrazu pole4, kde budou hodnoty vyssi nez 110.0 po predchozim navyseni o 30% a snizeni o 5
"""

pole = [100.10, 323.2, 355.9, 214.19, 87.0]
pole2 = list(map(lambda x: x * 1.3, pole))
print(pole2)

pole3 = list(filter(lambda x: x > 120.0, pole))
print(pole3)

pole4 = list(map(lambda x: x * 1.3 - 5, filter(lambda x: x > 110.0, pole)))
print(pole4)