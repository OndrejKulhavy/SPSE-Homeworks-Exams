import random

def velka(textak):
    return textak.upper()

def smajlik(textak):
    return textak.replace(" ", "😀")

def vw(textak):
    return textak.replace("V", "W")

def hvezda(textak):
    return f"*{textak}*"

def vykricnik(textak):
    textak = textak.replace("!", "!!!!!" * 5)
    textak = textak.replace("?", "???" * 3)
    return textak


funky_functions = [
    velka,
    smajlik,
    vw,
    hvezda,
    vykricnik
]

def funky_format(textak):
    selected_functions = random.sample(funky_functions, 3)
    result = textak
    for func in selected_functions:
        result = func(result)

    return result

print(funky_format("Ahoj Varle! Pudeme dnes do kina?"))