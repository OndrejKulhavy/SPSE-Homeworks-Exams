# 16.0
Pomocí knihovny NumPy vytvořte dvě pole hodnot, která budou obsahovat naměřené hodnoty časové a 
paměťové složitosti algoritmu brute-force ze cvičení 15.6. Pro řešení můžete použít ukázku vytvoření pole tří hodnot níže:

import numpy as np

a = np.array([0, 1, 2, 3])
b = np.array([0, 1, 5, 30])

print(a)
print(b)

# 16.1
Missing bro

# 16.2
Rozšiřte úlohu 16.1. pomocí knihovny NumPy tak, aby byla vytvořena tři pole, která ponesou název algoritmu z úlohy 
15.6. Tato pole budou vícerozměrná. V každém poli pak budou tři sady hodnot, první sada bude časová složitost, 
druhá sada bude paměťová a a poslední počet prvků (sedadel).

Následně napište algoritmus, který vypíše pro každé pole následující výpis (tj. vyfiltruje jen některé hodnoty):

Brute force, časová složitost [sec]: [0.2 1.4412 1.94724]

Monte carlo, časová složitost [sec]: [0.22 0.21 0.22]

Heuristika, časová složitost [sec]: [0.2 0.342 0.44]

# 16.3
S pomocí našich polí z příkladu 16.2 provedem následující operace:

1. Vypište všechny prvky paměťové složitost brute force vyjma prvního a posledního

2. Vypište posledních 5 prvků časové složitost monte carlo.

3. Vypište první prvek počtu sedadel, který jste měřili heuristice.
4. Nakonec si vyberte jedno pole a zjistěte co znamenají a co je níže uvedených vlastnostech tohoto pole:

.ndim
.shape
.dtype
.itemsize
.data

# 16.4
Přepodkládejte, že Vám někdo dal tři naměřené hodnoty takto definované:

import numpy as np

brute_force = np.array([1, 2, 3, 0.1932, 1.1247, 2.2435, 2243, 2124, 2143])
print(brute_force.shape)
1. Pomocí funkce reshape(..) upravte pole brute_force, aby obsahovalo třírozměrné pole a v každém rozměru byly tři prvky.

2. Pomocí funkce np.array_split(..) z knihovny NumPy vytvořte tři nová oddělená pole s hodnotami z ukázky,
3. která pojmenujete velikost, spotreba_cas, a spotreba_pamet,.

3. Pomocí funkce np.concatenate(..) spojte tři pole z bodu 2. zpět do jednoho.

4. Spusťte příklad níže a vyzkoušejete spojení níže uvedené druhy spojení pomocí zásobníku. U každého zkuste odvodit co se stalo:

 #spojeni po ose 1
vysledek = np.stack((velikost, spotreba_cas, spotreba_pamet), axis=1)

 #vertikalni spojeni, po sloupcich
vysledek = np.vstack((velikost, spotreba_cas, spotreba_pamet)) 

#horizontalni spojeni, po radcich
vysledek = np.hstack((velikost, spotreba_cas, spotreba_pamet))  

#spojeni do hloubky, po rozmerech
vysledek = np.dstack((velikost, spotreba_cas, spotreba_pamet))  

# 16.5
Přepodkládejte následující zdrojový kód:

import numpy as np
data = np.array([0.1743, 0.2732, 0.3521, 0.4924])
1. Vytvořte pole s názvem filter, které bude obsahovat čtyři prvky hodnot True,False,True,False.

2. Spusťe příkaz filtrace:

nova_data = data[filter]
3. Vypište nová data a stará data zjistěte jak pracuje filtrace. 

Skalární násobení

4. Jedním príkazem nyní všechny prvky v poli data vynásobte 1000 pomocí operátoru *

5. Od všech prvků odečťete číslo 1 pomocí operátoru -

6. K poli přičtěte jiné pole stejné velikosti vytovřené pomécí metody array knihovny NumPy pomocí operátoru +

7. Proveďte příkaz:

pripraveny_filtr = data < 0.25
A zjistete co se do promenne ulozilo.

# 16.6
Předpokládejme následující pole:

data = np.array([20,23,-100,-5,30,70,-18,99,81,16,45,90,-39,-82,75,0,16,91,48,0,70])
S polem proveďte následující cvičení:

1. Pomocí funkce where v knihovně NumPy vyberte jen záporná čísla.

2. Pomocí funkce where v knihovně NumPy vynerta jen čísla v rozsahu -10 až -1. 
(Nápověda: použijte kulaté závorky a znak &)

3. Pomocí funkce where v knihovně NumPy vynerta jen čísla v rozsahu 1 až 50, nebo čísla záporná.
(Nápověda: použijte kulaté závorky a znak |)