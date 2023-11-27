"""
Vytvořte funkci, která bude uložena v proměnné x a stejně jako v příkladu 9.1. bude počítat druhou mocninu ale
tentokrát bez toho, aby funkce měla svou definici s názvem pomocí příkazu def.
Využijte anonymní lambda konstrukci, která Vám do proměnné umožní uložit funkci přímo, aniž byste ji museli pojmenovat.
Následně otestujte spuštění příkazem x(3)
"""

x = lambda x: x**2

print(x(3))