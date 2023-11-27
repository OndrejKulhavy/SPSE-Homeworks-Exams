"""
Přepodkládejte následující kolekci:

zbozi = [
    {
        "name" : "IPHONE 14",
        "price" : 22169.0,
        "cathegory" : (12, "Mobilní telefony")
    },
    {
        "name" : "Fujifilm XT30",
        "price" : 22269.0,
        "cathegory" : (2, "Fotoaparáty")
    },
    {
        "name" : "Niceboy HIVE Pins Black",
        "price" : 999.0,
        "cathegory" : (4, "Sluchátka")
    }
]
Pomocí funkce sorted(zbozi, .... ) seřaďte zboží:

podle ceny vzestupně
podle názvu sestupně
podle pořadí kategorie vzestupně
"""

zbozi = [
    {
        "name" : "IPHONE 14",
        "price" : 22169.0,
        "cathegory" : (12, "Mobilní telefony")
    },
    {
        "name" : "Fujifilm XT30",
        "price" : 22269.0,
        "cathegory" : (2, "Fotoaparáty")
    },
    {
        "name" : "Niceboy HIVE Pins Black",
        "price" : 999.0,
        "cathegory" : (4, "Sluchátka")
    }
]

print("Sorted by price")
print(sorted(zbozi, key=lambda x: x["price"]))
print("Sorted be name descending")
print(sorted(zbozi, key=lambda x: x["name"], reverse=True))
print("Sorted by category")
print(sorted(zbozi, key=lambda x: x["cathegory"][0]))
