def formatuj_prijimeni_prvni(jmeno, prijmeni):
    return prijmeni + " " + jmeno

#print(formatuj_prijimeni_prvni("Jan", "Novak") )

def formatuj_monogram(jmeno, prijmeni):
    return jmeno[0] + "." + prijmeni[0] + "."

#print(formatuj_monogram("Jan", "Novak"))

def vyber_formatovaci_funkci(delka):
    if delka < 4:
        return formatuj_monogram
    else:
        return formatuj_prijimeni_prvni


formatovac = vyber_formatovaci_funkci(3)
print(formatovac("Jan", "Novak"))
formatovac = vyber_formatovaci_funkci(155)
print(formatovac("Jan", "Novak"))
