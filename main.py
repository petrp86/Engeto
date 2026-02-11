TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

user = ["bob", "ann", "mike", "liz",]
password = ["123", "pass123", "password123", "pass123",]
registered = False
oddelovac = 60 * "-"

jmeno = input("Zadej jméno: ").lower()
heslo = input("Zadej heslo: ")

print(oddelovac)

if not jmeno in user:
    print("Nejsi registrován! Program bude ukončen.")
else:
    pas = user.index(jmeno)
    if heslo == password[pas]:  # Porovnání shody jména a hesla.
        registered = True
        print("Vítej uživateli", jmeno)
    else:
        print("Zadal jsi špatné heslo!")

if registered:
    num = input("Vyber číslo textu, který chceš analyzovat (1-3): ")
    if not num:  # Žádný vstup.
        print("Nic jsi nevybral.")
    elif not num.isdigit():  # Nebylo zadáno číslo.
        print("Zadal jsi jiný vstup.")
    elif not int(num) in range(1, 4):  # Nebylo zadáno číslo z rozsahu.
        print("Nezadal jsi správné číslo.")
    else:
        num = int(num) - 1

        print(oddelovac)

        text = TEXTS[num]  # Výběr textu k analýze.
        text = text.split( )  # Rozdělení textu na slova.
        POCET_SLOV = len(text)  # Zjištění počtu slov v textu.
        prvni_velke = 0  # Počet slov titlecase.
        vsechna_velka = 0  # Počet slov uppercase.
        vsechna_mala = 0  # Počet slov lowercase.
        cisla = 0  # Počet čísel.
        soucet = 0  # Součet čísel.
        seznam_delek = set()  # Množina délek slov.
        pocet_delek = {}  # Slovník s počtem slov určité délky.
        delka_slova = 0

        for slovo in text:  # Pro každé slovo v textu proveď --->
            slovo = slovo.strip(",").strip(".").strip("!").strip("?")
            seznam_delek.add(len(slovo))  # Přidání délky slova do množiny délek.
            pocet_delek[len(slovo)] = pocet_delek.get(len(slovo), 0) + 1  
            # Přiřazení počtu slov k délce slova
            if slovo.istitle():
                prvni_velke = prvni_velke + 1
            elif slovo.isupper():
                vsechna_velka = vsechna_velka + 1
            elif slovo.islower():
                vsechna_mala = vsechna_mala + 1
            elif slovo.isdigit():
                cisla = cisla + 1
                soucet = soucet + int(slovo)
        else:
            print(f"Slov je v textu {POCET_SLOV}.")
            print(f"Slov začínajících velkým písmenem je v textu {prvni_velke}.")
            print(f"Slov napsaných velkými písmeny je v textu {vsechna_velka}.")
            print(f"Slov napsaných malými písmeny je v textu {vsechna_mala}.")
            print(f"Čísel je v textu {cisla}.")
            print(f"Součet všech čísel v textu je {soucet}.")
            print(60 * "-")
            max_delka = max(pocet_delek.values()) + 5  
            # Zjištění max počtu slov o stejné délce pro odsazení.
            for delka_slova in seznam_delek:
                hvezdy = "*" * pocet_delek[delka_slova]
                print(str(delka_slova).rjust(2), "|", hvezdy.ljust(max_delka),
                "|", str(pocet_delek[delka_slova]))