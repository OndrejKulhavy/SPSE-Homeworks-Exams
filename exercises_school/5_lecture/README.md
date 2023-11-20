## Cvičení č.5
16-10-2023

---

## Zadání 1
[Script.py](exercise_1.py)

Naprogramujte třídu, která reprezentuje láhev a která má:
1) vlastnost kapacity v litrech a vlastnost, která určuje objem kapaliny v lahvi opět v litrech. 
2) konstruktor, který umožní nastavit kapacitu lahve a nastaví, že je lahev prázdná.
3) metody, která umožní nastavit i získat objem v litrech tak, aby nikdy objem kapaliny v lahvi nepřekročil její kapacitu.
4) metodu pro vyprázdnění obsahu láhve.
5) metody, která umožní nastavit i získat objem kapaliny v mililitrech tak, aby nikdy objem kapaliny v lahvi nepřekročil její kapacitu.
6) mechanismus uzavření láhve tak, aby láhev mohla být ve dvou stavech: zavřená a otevřená. Ve stavu zavřená nelze měnit objem kapaliny ani láhev vyprázdnit a ve stavu otevřená to možné je. Nezapomeňte upravit předchozí metody tak, aby zohledňovali stav.

## Zadání 2
[Script.py](exercise_2_and_3.py)

Oživte následující zdrojový kód, který reprezentuje jednoduchý systém vstupu do školní budovy

```python
d = Dvere(zamceno=True)
try:
    d.otevrit()
    print("Prosel jsem")   
except ZamceneDvereException as e:
    print("Dvere jsou zamcene, nemuzes je otevrit")
```

## Zadání 3
[Script.py](exercise_2_and_3.py)

Upravte ulohu "Dveře" tak, aby program na závěr vypsal, jestli uživatel dveřmi prošel či nikoliv. Tato informace se vypíše, ať už uživatel dveřmi prošel nebo neprošel (dveře jsou zamčené, došlo k vyhození výjimky ZamceneDvereException)

Doplnění sekce finally do konstrukce try/except.

## Zadání 4
[Script.py](linked_list.py)

Bez použití příkazu import (tj. bez knihoven třetích stran) naprogramujte jednosměrný spojový seznam, který naplníte min. 5 prvky a pak napíšete algoritmus který vypíše všechny prvky na obrazovku.

## Zadání 8
[Script.py](exercise_8.py)
```python
class Auto:
    """ Trida auto reprezentuje auto pro simulaci realneho vozidlo pro cviceni PV na SPSE Jecna """

    def __init__(self, objem_nadrze_l : float, spotreba_na_100_km_l : float):
        """
        Konstruktor nastavi objem nadrze a spotrebu dle parametru a nastavi prazdnou nadrz.

        :param objem_nadrze_l: Objem nadrze v litrech
        :param spotreba_na_100_km_l: Spotreba na 100km v litrech
        """

        if (objem_nadrze_l < 0):
            raise Exception("Nadrz musi mit kladny objem")
        if (spotreba_na_100_km_l < 0):
            raise Exception("Spotreba nesmi byt zaporna")

        self.objem_nadrze_l = objem_nadrze_l
        self.spotreba_na_100_km_l = spotreba_na_100_km_l
        self._aktualni_objem_paliva_v_nadrzi_l = 0

    def aktualni_stav_nadrze(self) -> float:
        """
        Metoda vrati aktualni stav nadrze

        :return: Zbyle palivo v nadrzi v litrech
        """
        return self._aktualni_objem_paliva_v_nadrzi_l

    def natankuj(self, objem_l : float ) -> None:
        if(objem_l < 0):
            raise Exception("Nelze odcerpat palivo pomoci metody natankovat")

        if((self._aktualni_objem_paliva_v_nadrzi_l + objem_l) > self.objem_nadrze_l):
            raise Exception("Nelze nacerpat vice nez je kapacita nadrze")

        self._aktualni_objem_paliva_v_nadrzi_l += objem_l

    def popojed(self, pocet_km : float ) -> None:
        if(pocet_km < 0):
            raise Exception("Couvani je take jizda, smer neresime")

        spotreba_paliva_l = pocet_km/100.0 * self.spotreba_na_100_km_l

        if(self._aktualni_objem_paliva_v_nadrzi_l < spotreba_paliva_l):
            raise Exception("Na jizdu neni dostatek paliva")

        self._aktualni_objem_paliva_v_nadrzi_l -= spotreba_paliva_l
```
Napište zdrojový kód, který:

- vytvoří auto s nádrží na 30l a spotřebou 12,5l/100km;
- nastaví objem paliva nádrže na 22,5l
- sníží objem paliva jizdou na 20km -2,5l
- Promyslete si odpovědi na následující otázky:

- Jaké jsou atributy/vlastnosti třídy?
- Jaké atributy/vlastnosti třídy jsou public a jaké private?
- Jak je řešen ve třídě princip zapouzdření, jak se manipuluje s private atributy?

## Zadání 9
[Script.py](exercise_8.py)
V úloze 5.6. jste mohli vidět ukázku správného použití dokumentace tříd pomocí pydoc. 

Vaším 1. úkolem je doplnit dokumentaci metodám natankuj() a popojed() tak, aby byly vždy jasné tři věci:
1) Jaký je smysl metody? Celý její zdrojový kód shrňte jednou větou.
2) Jaké jsou vstupy metody? Pro každý vstup napište na samostaný řádek :param <nazev parametru>: <popis parametru> Pozor na správný zápis dvojteček.
3) Jaké jsou výstupy metody? Pro výstup napište na samostaný řádek :return: <popis navratove hodnoty> Pozor na správný zápis dvojteček.
Výsledek můžete zkontrolovat v PyCharm tak, že na najedete myší na název metody v kódu, kde ji používáte a prohlédnete si, zda-li PyCharm dokumentaci správně načetl.

Vaším 2. úkolem je rozšířit třídu Auto o private atribut, který eviduje kolim km auto najelo. Při vytvoření má auto najeto 0km a pomocí metody popojed() se hodnota bude zvyšovat. Do třídy musíte také přidat novou metodu aktualni_stav_najetych_km(), která bude vracet, kolik km auto najelo. 

Nezapomeťe při každém rozšíření třídy, úpravy metody nebo vytvoření nové metody, či vlastnosti upravitnaj především dokumentaci.
## Zadání 10
[Script.py](exercise_9.py)

V jazyce python je to s konstruktory mírně jinak, než je to v Jave a C#. V pythonu existují dvě dunder (dunder je zkratka double underscore) metody. Jsou to speciální metody:
```python
__new__(cls, ...)
__init__(self, ...)
Metoda __new__(cls, ...)
```
Je statická metoda, která se volá automaticky před vytvořením instance v operační paměti. 

Pomocí ní můžete totiž ovlivnit jak se instance vytvoří a zdali se vůbec vytvoří. Je to krásná implementace návrhového vzoru factory method pattern. Metodu zpravidla nepoužijete, tedy nebude ji psát, ale pokud ano musít v ní ručně napsat práve vytvoření instance a to tak, že zavoláte jinou metody __new__ v rodičovské třídě a předáte ji název této třídy. Název třídy se ukládá do proměnné cls, a k rodičovské třídě můžete přes super(). Například takto:

```python
class MyClass:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance
```
Metoda `__init__(self, ...)`
Je statická metoda, která se volá automaticky po vytvoření instance v operační paměti. Pomocí ní můžete vytvářet vlastnosti třídy. Pozor toto je odlišné od jazyka Java i C#, kde jste vlastnosti staticky deklarovali. V pythonu ne. V pythonu je dynamicky vytoříte až po vytvoření objektu. Například takto udělám dvě vlastnosti foo a bar do kterých dám defaultní hodnoty třeba "ahoj" a "svete"
```python
class MyClass:
    def __init__(self, *args, **kwargs):
        self.foo = "ahoj"
        self.bar = "svete"
```     
Příklad 

Se podívejte, jak lze tyto metody využít u třídy zboží, kde se bráníme jednoduchému hacku, kde nechceme vůbec povolit vytvoření objketu v paměti se zápornou cenou
```python
class Zbozi:
    def __new__(cls, nazev, cena):
        if cena < 0:
            instance = None
        else:
            instance = super().__new__(cls)
        
        return instance

    def __init__(self, nazev, cena):
        self.nazev = nazev
        self.cena = cena

a = Zbozi("Rohlik", 5)
b = Zbozi("Hackers item", -10)

print(a)
print(b)
```
Vaším úkolem je vylepšit kód tak, aby:
Nebylo možné vytvořit ani zboží bez názvu
Nebylo možné vytvořit zboží, které bude mít cenu uvedenou jako něco, co není číslem

## Zadání 11
[Script.py](exercise_11.py)
Dunder metody, jsou speciální (magické) metody, které se v Pythonu zapisují pomocí dvou podtržítek před i za názvem třídy. Ukažme si jednoduchý příklad dobře známé metody  __str__(). Předpokládaje třídu definovanou takto:
```python
import re

class BankovniUcet:
    """ Trida ukazuje simulaci bankovniho uctu """

    def __init__(self, cislo_uctu : str, mena : str ):
        """
        Konstruktor prijima cislo uctu a menu, ve ktere je vedeny.

        :param cislo_uctu: Cislo uctu i kod banky ve formatu 5-10 cislic / 4 cislice
        :param mena: Mena uctu vyjadrena jako tri pismena, napr. EUR
        """
        if not re.match(r"^[0-9]{5,10}/[0-9]{4}$",cislo_uctu):
            raise Exception('Cislo uctu neodpovida formatu zapisu 000000000/0000.')

        if not re.match(r"^[A-Z]{3}$", mena):
            raise Exception('Mena neodpovida formatu zapisu tri velkych pismen.')

        self._cislo_uctu = cislo_uctu
        self._mena = mena
        self._zustatek = 0
```
Vaším úkolem je doplnit do třídy dunder/magickou metody __str__(self) i s dokumentací tak, aby metoda vypsala cislo uctu a za dvojteckou zustatek a menu. Otestovat můžete svůj kód následujícím příkazem:
```python
ucet_alice = BankovniUcet("12341238/0100","CZK")
print(ucet_alice)
```
Následně přidejte i implementaci metod ` __int__(self) a __float__(self) ` aby bylo mozne tridu prevest na cislo. Pri prevodu se prevede zustatek. Otestovat to muzete napriklad:
```python
zustatek_alice = int(ucet_alice)
print(zustatek_alice)
```

## Zadání 12
[Script.py](exercise_12.py)

Předpokládejme následující zdrojový kód:
```python
import re

class PenezniHotovost:
    """
    Trida reprezentuje penezni hotovost v urcite mene
    """

    def __init__(self, castka: float, mena: str):
        """
        Pri vytvoreni tridy se musi specifikovat castka a mena, nebo se pouzije defaultnich 0 EUR

        :param castka: Jakekoli realne cislo, muze byt i zaporne
        :param mena: Mena vyjadrena jako tripismeny kod
        :return: Objekt penezni hotovosti
        """
        if not re.match(r"^[A-Z]{3}$", mena):
            raise Exception('Mena neodpovida formatu zapisu tri velkych pismen.')

        self._mena = mena
        self._castka = castka

    def __str__(self):
        """
        Vrati castku a menu jako string
        :return: <castka> <mena>
        """
        return str(self._castka)+" "+self._mena

    def __add__(self, other):
        """
        Pretizeni operatoru + ktere vytvori novy objekt jako vysledek operace scitnai
        :param other: Lze scitat cisla typy int, float nebo jiny objekt penezni hotovosti ve stejne mene
        :return: Vraci novy objekt, ktery ma nastavenou menu podle puvodnich objektu a zustatek jako vysledek operace scitani
        """
        if(isinstance(other, float) or isinstance(other, int)):
            vysledek = PenezniHotovost(0, self._mena)
            vysledek._castka = self._castka + other
            return vysledek

        if(isinstance(other, PenezniHotovost) and other._mena == self._mena):
            vysledek = PenezniHotovost(0, self._mena)
            vysledek._castka = self._castka + other._castka
            return vysledek

        raise Exception("Penezni hotovost lze scitat pouze s int,float a hotovosti ve stejne mene")
```
Ten zdrojový kód implementuje dvě dunder/magické metodu. Jednu pro konverzi na string __str__ a druhá pro přetížení operátoru pro sčítání +. Funkčnost lze otestovat:
```python
sto_korun = PenezniHotovost(100, "CZK")
dve_sta_korun = sto_korun + 100

print(sto_korun)
print(dve_sta_korun)
```
Všiměte si, že stejně jako v matematice sčítáním dvou hodnot vzniká nová hodnota, třetí. Tedy metoda __add__ pracuje stejným způsobem sčítá sama sebe self se vstupní proměnnou other, kterou nejprve zkontroluje, protože ne vše lze sčítat. Nakonec vytvoří novou instanci třídy PenezniHotovost, nastaví do ní výsledné hodnoty a vrátí ji. Stejný výsledek bychom dokázali přímým voláním: dve_sta_korun = sto_korun.__add__(100)

Vaše úkoly jsou následující, doprogramujte další metody:
Odečítání operátorem - a metodou `__sub__(self, other)`
Násobení operátorem * a metodou `__mul__(self, other)`
Mocnění operátorem ** a metodou `__pow__(self, power, modulo=None)`
Pro jedničkáře, můžete zkusit i dělení, nicméně je třeba vědet, že je ho více druhů celočíselné, modulo apod... 

## Zadání 13
[Script.py](exercise_13.py)

Rozšiřte třídu PenezniHotovost z předchozí úlohy o metody, které lze spouštět pomocí operátoru +=, -=, *= aby fungoval tento kód:
```python
vyplata = PenezniHotovost(1000, "CZK")
vyplata += 2000 #1000 + 2000 = 3000
vyplata -= 500 #3000 - 500 = 2500
vyplata *= 2 #2500 * 2 = 5000
print(vyplata) #ma vypsat 5000
```
I když teoreticky může fungovat výše uvedený kód i s metodami z předchozího cvičení, nezapomeňme, že například operátor A + B vytváří nový objekt C, nicméně opetátor A += B naopak pouze mění objekt A, tedy výsledkem operace je vrácení objektu self, například pro dělení by to bylo takto:
```python
def __truediv__(self, other):
    """
    Implementace operatori /= ma za ukol vydelit hotovost a zachovat puvodni objekt
    :param other: Muze byt int, float nebo trida PenezniHotovost 
    :return: Vraci stavajici objekt, ktery ma nastavenou menu podle puvodnich objektu a zustatek jako vysledek operace deleni
    """
    if(isinstance(other, float) or isinstance(other, int)):
        self._castka /= other
        return self

    if(isinstance(other, PenezniHotovost) and other._mena == self._mena):
        self._castka /= other._castka
        return self

    raise Exception("Penezni hotovost lze scitat pouze s int,float a hotovosti ve stejne mene")
```
Otestova to lze například takto:
```python
vyplata = PenezniHotovost(1000, "CZK")
vyplata /= 2 
print(vyplata)
```

## Zadání 14
[Script.py](exercise_14.py)

Uvažujte následující zdrojový kód:

```python
import re
class Zbozi:
    """ Trida zbozi pro ukazu prikladu relacnich operatoru"""

    def __init__(self, nazev: str, vaha: float):
        """
        Pri vytvoreni se nastavuje nazev zbozi a jeho vaha
        :param nazev: Nazev musi byt znaky v rozsahu 1 az 200 znaku
        :param vaha: Vaha musi byt kladne a nenulove cislo
        """
        if not re.match(r"^[\D ]{1,200}$", nazev):
            raise Exception('Nazev musi byt v rozsahu 1 az 200 znaku')
        if vaha <= 0:
            raise Exception('Vaha nesmi byt zapojna')

        self._nazev = nazev
        self._vaha = vaha

    def __lt__(self, other):
        """
        Metoda zjistuje jestli je zbozi mensi nez druhe zbozi. Porovnava se pouze vaha.
        :param other: Trida pro porovnani, musi to byt instance Zbozi
        :return: True pokud je self mensi nez other
        """
        if (not isinstance(other, Zbozi)):
            raise Exception('Porovnavat lze jen zbozi mezi sebou')

        return self._vaha < other._vaha
        
```
V této ukázce je vyřešeno porovnání operátorem <, otestovat to můžeme například takto:

```python
kilo_brambor = Zbozi("Bramobra", 1)
krabice_mleka = Zbozi("Mleko", 1.029)
if(kilo_brambor < krabice_mleka):
    print("Svet je jeste v poradku")
```

Vaším úkolem je rozšířit třídu zboří tak, aby stejným způsobem fungovala i pro operátory:

Operátor `>` pomocí metody `__gt__(self, other)`

Operátor `<=` pomocí metody `__le__(self, other)`

Operátor `>=` pomocí metody `__ge__(self, other)`

Operátor `==` pomocí metody `__eq__(self, other)`

Operátor `!=` pomocí metody `__ne__(self, other)`

## Zadání 15
[Script.py](exercise_15.py)

Upravte předchozí úlohu se zbožím tak, že doplníte metodu __hash__(self), která vrátí unikátní hash (tj. číslo) na základě názvu i váhy. Lze to otestovat voláním:
```python
zbozi1 = Zbozi("Mrkev", 1)
print(hash(zbozi1))
```
Následně ovládněte pomocí metod `__eq__` a `__hash__` to jak se bude chovat na vložení těchto objektů kolekce typu `set()`. Pro otestování vytovříme tři objekty o stejné váze, ale jen dva budou mít stejný název a zkusíme je přidat do kolekce. Cílem je, aby se přidali jen dva znich:
```python
zbozi1 = Zbozi("Mrkev", 1)
zbozi2 = Zbozi("Mrkev", 1)
zbozi3 = Zbozi("Celer", 1)

x = set()
x.add(zbozi1)
x.add(zbozi2)
x.add(zbozi3)
print(len(x))
```
Pro úspěšné vyřazení ze set() jako duplicita je třeba aby oba objekty měli shodný hash a také aby operátor == tedy metoda __eq__ vracel True.

## Zadání 16
[Script.py](exercise_16.py)

Rozšiřte Váš domácí úkol ve kterém jste vytvořil(a) třídu pro reprezentaci jednosměrného, nebo obousměrného spojového seznamu dle svého uvážení tak, aby bylo možné používat frontu pomocí níže uvedených operátorů:
 
Přetížení funkce pro počet prvků fronty klasickým způsobem len() pomocí metody __len__(self), otestovat lze například print(len(fronta)) vrátí pořet prvků
Přetížení hranatých závorek [] pomocí metody __getitem__(self, key), otestovat lze například print(fronta[3]) vrátí 4. prvek
Přetížení hranatých závorek [] pomocí metody __setitem__(self, key, value), otestovat lze například fronta[0]="Pepa" nastaví první prvek na "Pepa"



