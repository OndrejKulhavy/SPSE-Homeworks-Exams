## 1. Exercise

Předpokládejte následující zdrojový kód:
```python
import time

def vypis_cisel():
    for i in range(0,10):
        print(i)
        time.sleep(1)

if __name__ == "__main__":
    print("ZACATEK PROGRAMU")
    vypis_cisel()
    print("KONEC PROGRAMU")
   ```
Zkuste ho spustit. Pozorujte jak program vypisuje každou sekundu jedno číslo. Na začátku vypíše ZACATEK PROGRAMU  a na konci KONEC PROGRAMU. Nyní zkusíme tento program paralelizovat tak že volání metody vypis_cisel() nahradíme spuštěním paralelního procesu.

1. Nejprve doplňte import knihovny pro paralelní procesy v Pythonu takto:

import time
import multiprocessing
2. Metodu pro vypis cisel nechame stejnou

3. Nahraďme místo v main konstrukci, kde se volá  vypis_cisel() spuštěním paralelního procesu například takto:
```python

if __name__ == "__main__":
  print("ZACATEK PROGRAMU")
  p1 = multiprocessing.Process(target=vypis_cisel)
  p1.start()
  print("KONEC PROGRAMU")

```    
Pozorujte co se změnilo a pokuste se odpovědět na následující otázky:

Je v programu chyba když vypisuje KONEC PROGRAMU dříve než skončí? 
Kolik paralelních procesů bylo vlastně spuštěno? Jeden nebo dva?