"""
Napište funkci save_csv(company_name, ico, phones, description), která uloží do souboru CSV záznam o firmě. Program musí být schopen obsloužit následující tři příkazy:

save_csv("SPSE Jecna", 61385301, ["224941469","224942066"], Škola nabízí obory:
- Informatika
- Elektrotechnika
a její ředitel říka: "Je to nejlepší škola v Praze".
)

save_csv("Seznam.cz", 26168685, "234694111", None)

save_csv("PPF A.S", 25099345, None, "Zkratka 'PPF' znamená první privatizační fond."]
Následně ze souboru načtěte pouze firmy, které mají vypněný popis a vypište jejich názvy a IČO.
"""

import csv


def save_csv(company_name, ico, phones, description):
    with open('firmy.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([company_name, ico, phones, description])


def load_csv():
    companies_with_empty_description = []

    with open('firmy.csv', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            company_name, ico, phones, description = row
            if description is None or description.strip() == "":
                companies_with_empty_description.append((company_name, ico))

    return companies_with_empty_description


save_csv("SPSE Jecna", 61385301, ["224941469", "224942066"], """Škola nabízí obory: 
- Informatika
- Elektrotechnika
a její ředitel říka: "Je to nejlepší škola v Praze".
""")

save_csv("Seznam.cz", 26168685, "234694111", None)

save_csv("PPF A.S", 25099345, None, "Zkratka 'PPF' znamená první privatizační fond.")
companies_with_empty_description = load_csv()

# Vypsání firem
print("Firmy s vypnutým popisem:")
for company_name, ico in companies_with_empty_description:
    print(f"Název: {company_name}, IČO: {ico}")
