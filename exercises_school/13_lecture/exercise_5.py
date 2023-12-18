"""
Vytvořte v pythonu samostatný modul a v něm třídu, která reprezentujte uživateský profil s
názvem SchoolProfile a má atributy jméno, příjmení, username, favorite_school_subject, favorite_school, favorite_teacher.
Třída musí mít metodu toString()
Vytvořte skript main1.py a v něm importujte třídu SchoolProfile a vytvořte instanci profilu,
který reprezentuje Vašeho nevíce oblíbeného spolužáka a tuto instanci serializujte (uložte do souboru) my_favorite_friend.dat pomocí modulu pickle.
Vytvořte skript main2.py a v něm načtěte ze souboru my_favorite_friend.dat
instanci třídy SchoolProfile vypište ji na obrazovku.
"""

from school.school_profile import SchoolProfile
import pickle

profile = SchoolProfile("Jan", "Novák", "jnovak", "matematika", "SPŠE Jecna", "Mgr. Jan Novák")
with open("my_favorite_friend.dat", "wb") as file:
    pickle.dump(profile, file)

with open("my_favorite_friend.dat", "rb") as file:
    profile = pickle.load(file)
    print(profile)
