"""
Napište generátor, který bude při spuštění
kódu níže vypisovat jména třech největších osobností ze světa IT:
"""


def generator_of_famous_people_in_it():
    yield "Bill Gates"
    yield "Steve Jobs"
    yield "Steve Wozniak"
    StopIteration()


if __name__ == "__main__":
    print("Velikani v IT")
for person in generator_of_famous_people_in_it():
    print(person)
