import random


def vytvor_cislo(cislo: int) -> str:
    """
    Vytvoří náhodné čtyřciferné číslo
    """
    nahodne_cislo = str(random.choice(x))

    return nahodne_cislo


def overeni_cisla(cislo: str) -> bool:
    """
    Ověří správnost čísla dle požadavků:
    1. musí mít správnou délku
    2. musí to být číslo
    3. nesmí začínat nulou ale může ji obsahovat
    4. má unikátní číslice (nesmí se opakovat)
    """
    set_cisla = set(cislo)
    vstup_ok1 = False if len(cislo) != 4 else True
    vstup_ok2 = False if not cislo.isdigit() else True
    vstup_ok3 = False if cislo[0] == "0" else True
    vstup_ok4 = False if len(set_cisla) != len(cislo) else True
    vstup_ok = vstup_ok1 and vstup_ok2 and vstup_ok3 and vstup_ok4

    return vstup_ok


def bull(a: str,b: str) -> int:
    """
    Zjistí počet uhodnutých bull/bulls
    """
    bulls = 0

    for x, y in zip(a, b):
        if x == y:
            bulls += 1

    return bulls


def cow(a: str, b: str) -> int:
    """
    Zjistí počet uhodnutých cow/cows
    """
    set_nahodne_cislo = set(a)
    set_zadane_cislo = set(b)
    porovnani = set(set_nahodne_cislo & set_zadane_cislo)
    cows = (len(porovnani)) - pocet_bulls

    return cows


oddelovac = 55 * "-"    # Oddělovač textu a pokusů
znova = "ano"

print(f"""
{oddelovac}
Ahoj!
{oddelovac}
Vygeneroval jsem pro tebe náhodné čtyřciferné číslo.
Pojď si zahrát hru \"Bulls&Cows\".
{oddelovac}""")

while znova == "ano":
    x = range(1000,9999)    # Rozsah pro vytvoření náhodného čísla
    nahodne_ok = False
    zadane_ok = False
    pokus = 0

    while not nahodne_ok:
        nahodne_cislo = vytvor_cislo(x)    # Vytvoření náhodného čísla
        nahodne_ok = overeni_cisla(nahodne_cislo)    # Ověření správných parametrů náhodného čísla

    while not zadane_ok:
        if pokus == 0:
            print("Zadej čtyřciferné číslo: ", oddelovac, sep="\n")    # Text pro první zadání uživatele
            zadane_cislo = input()    # Vstup od uživatele
        else:
            zadane_cislo = input()    # Vstup od uživatele
        pokus += 1
        zadane_ok = overeni_cisla(zadane_cislo)    # Ověření správných parametrů zadaného čísla uživatelem
        set_cisla = set(zadane_cislo)
        vstup_ok1 = False if len(zadane_cislo) == 4 else print("Nezadal jsi správnou délku!")
        vstup_ok2 = False if zadane_cislo.isdigit() else print("Nezadal jsi číslo!")
        vstup_ok3 = False if zadane_cislo[0] != "0" else print("Číslo nesmí začínat nulou!")
        vstup_ok4 = False if len(set_cisla) == len(zadane_cislo) else print("Číslice v čísle se nesmí opakovat!")
        if not zadane_ok:
            print("Zkus to znova: ", oddelovac, sep="\n")    # Text při vyhodnocení špatného zadání uživatele
        else:
            pocet_bulls = bull(nahodne_cislo, zadane_cislo)    # Počet bulls
            pocet_cows = cow(nahodne_cislo, zadane_cislo)    # Počet cows
            text_bull = "bull" if pocet_bulls == 1 else "bulls"    # Rozlišení jednotného/množného čísla bull/bulls
            text_cow = "cow" if pocet_cows == 1 else "cows"    # Rozlišení jednotného/množného čísla cow/cows
            print(pocet_bulls, text_bull, ", ", pocet_cows, text_cow)
            print(oddelovac)
            zadane_ok = False if pocet_bulls != 4 else True    # Ukončení hádaní při uhodnutí čísla
    else:
        znova = "ne"
        print(f"Gratuluji! Náhodné číslo bylo odhaleno.")
        print(f"Počet pokusů: {pokus}")
        znova = input("Chceš hrát znova? Zadej 'ano': ").lower()