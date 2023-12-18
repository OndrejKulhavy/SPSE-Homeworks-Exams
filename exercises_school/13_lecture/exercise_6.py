"""
Vytvořte program, který si bude pamatovat kolikrát byl už spuštěný a kdy byl spuštěn naposled. Tyto informace si musí program pamatovat v dictionary info dle formátu z ukázky, kde také naleznete způsob serializace těchto dat do binární podoby a deserializace zpět do objektu v jazyce Python.

import pickle
import datetime

#zakladni format info
info = { 'pocet_spusteni': 0, 'posledni_spusteni': None }

#po kazdem spusteni provest
info['pocet_spusteni'] += 1
info['posledni_spusteni'] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

#serializace do binarni podoby
serializovana_data = pickle.dumps( data )
print(serializovana_data)

#deserializace do objektu
data = pickle.loads( serializovana_data )
print(data)
Vaším úkolem je upravit ukázku, tak aby se serializovaná data zapisovala do binárního souboru info.dat a program skutečně vědel, kolikrát byl spuštěn a kdy.
"""

import pickle
import datetime

soubor_info = 'info.dat'

try:
    with open(soubor_info, 'rb') as file:
        info = pickle.load(file)
except FileNotFoundError:
    info = {'pocet_spusteni': 0, 'posledni_spusteni': None}

info['pocet_spusteni'] += 1
info['posledni_spusteni'] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

with open(soubor_info, 'wb') as file:
    pickle.dump(info, file)

with open(soubor_info, 'rb') as file:
    data = pickle.load(file)
    print(data)
