regions = {
    'Středočeský Kraj': {'Benešov', 'Beroun', 'Kladno', 'Kolín', 'Kutná Hora', 'Mělník', 'Příbram', 'Rakovník'},
    'Jihočeský Kraj': {'České Budějovice', 'Český Krumlov', 'Strakonice', 'Tábor', 'Jindřichův Hradec'},
    'Plzeňský Kraj': {'Domažlice', 'Klatovy', 'Plzeň', 'Rokycany', 'Tachov', 'Stříbro'}
}

def get_region_name(city_name):
    if not city_name:
        raise ValueError('City name can not be empty')
    for region_name, cities in regions.items():
        if city_name in cities:
            return region_name

def get_all_cities_in_region(region_name):
    if not region_name:
        raise ValueError('Region name can not be empty')
    return regions[region_name]

def ask_user_mode():
    choice = input("Do you want to search regions or cities? regions/cities")
    if choice == "regions" or choice == "cities":
        return choice
    else:
        return ask_user_mode()

try:
    choice = ask_user_mode()
    if choice == "regions":
        city_name = input("Enter city name: ")
        region_name = get_region_name(city_name)
        print(region_name)
    elif choice == "cities":
        region_name = input("Enter region name: ")
        cities = get_all_cities_in_region(region_name)
        print(cities)
except ValueError as e:
    print(e)
