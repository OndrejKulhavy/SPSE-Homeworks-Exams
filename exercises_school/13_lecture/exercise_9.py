import json


def save_json(company_name, ico, phones, description):
    data = {}
    try:
        with open('firmy.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        pass

    data[company_name] = {
        'ico':         ico,
        'phones':      phones,
        'description': description
    }

    with open('firmy.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def load_json():
    companies_with_empty_description = []

    with open('firmy.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        for company_name, company_data in data.items():
            if company_data['description'] is None or company_data['description'].strip() == "":
                companies_with_empty_description.append((company_name, company_data['ico']))

    return companies_with_empty_description


save_json("SPSE Jecna", 61385301, ["224941469", "224942066"], """Škola nabízí obory:
- Informatika
- Elektrotechnika
a její ředitel říka: "Je to nejlepší škola v Praze".
""")

save_json("Seznam.cz", 26168685, "234694111", None)

save_json("PPF A.S", 25099345, None, "Zkratka 'PPF' znamená první privatizační fond.")
