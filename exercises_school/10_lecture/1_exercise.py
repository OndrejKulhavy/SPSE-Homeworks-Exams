"""
Nadefinujte funkci z názvem druha_mocnina, která přijme jeden číselný parametr a spočítá jeho druhou mocninu. Funkci otestujte příkazem druha_mocnina(3)
Vytvořte proměnnou x = ... do které místo těchto třech teček uložíte funkci mocnina. Vytvoříte tak prakticky ukazatel na funkci. Ukazatel otestujte příkazem x(3)
Vytvořte proměnnou y = x a otestujte zda-li může ukazatel na funkci ukazovat na další ukazatel a otestujte příkaz y(3)
"""


def druha_mocnina(x):
    return x * x


x = druha_mocnina

print(x(3))

y = x

print(y(3))
