"""

Upravte ulohu 4.2 s využítím metody next(), tak aby vypisovala
 rašelinná jezera bez použití for cyklu
  (namisto nej pouzite cyklus while).
"""


def generator_raselinnovych_jezer_CR():
    yield "Horní macošské jezírko"
    yield "Dolní macošské jezírko"
    yield "jezírko v Hranické propasti"
    yield "Bozkovské podzemní jezero"
    yield "Točnické jezírko"


def generator_cities():
    yield "Praha"
    yield "Brno"
    yield "Ostrava"


if __name__ == "__main__":
    cities = generator_cities()

    while True:
        try:
            print(next(cities))
        except StopIteration:
            break
