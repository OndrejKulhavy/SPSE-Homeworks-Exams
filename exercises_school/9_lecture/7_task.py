"""
Generátory jsou specifickou ukázkou mnohem mocnější kategorie funkcí/metod, než si možná nyní dokážete představit. Než se do toho pustíme tak trochu teorie:

Sub-rutine (česky pod-program, metoda nebo funkce) je například funkce, níže:

def vydej_obedu():
    menu = [
         "vitamínový nápoj",
         "polévka česneková s bramborem",
         "segedínský guláš, houskové knedlíky",
         "jablko",
    ]
    return menu
Když takovou metodu zavoláme 2x tak dvakrát proběhne celá najednou. Například takto:

print(vydej_obedu())
print(vydej_obedu())
Co-rutine (česky ko-program) je naopak funkce, která když se zavolá poprvé nemusí proběhnout celá najednou. Může například udělat jen dva, nebo tři příkazy, pak se přeruší, tedy vrátí se do původního programu a když ji někdo zavolá podruhé tak práci dokončí.

Zkuste tedy upravit výše uvedenou metodu vydej_obedu() tak, aby po prvním zavolání vrátila jen nápoj a až po druhém zbytek jídel. Samozřejmě, ž spuštění musí být mírně odlišné. Otestovat to můžete například následujícím kódem:

corutina1 = vydej_obedu();
napoje = next(corutina1)
print(napoje)
jidla = next(corutina1)
print(jidla)
"""


def catch_lunch():
    menu = [
         "vitamínový nápoj",
         "polévka česneková s bramborem",
         "segedínský guláš, houskové knedlíky",
         "jablko",
    ]
    yield [menu[0]]
    yield [menu[1], menu[1], menu[3]]


corutina1 = catch_lunch()

napoje = next(corutina1)
print(napoje)
jidla = next(corutina1)
print(jidla)
