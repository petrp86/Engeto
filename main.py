import random


def vytvor_cislo() -> str:
    """
    Vytvoří náhodné číslo, které nezačíná nulou
    a číslice v něm se neopakují.
    """    
    while True:
        cislo = "".join(random.sample(CISLICE, POCET_CIFER))
        if cislo[0] != "0":
            break
    
    return cislo


def over_cislo(cislo: str) -> list:
    """
    Ověří správnost čísla a vrátí list chyb v zadání
    dle požadavků:
    1. nesmí být prázdný vstup
    2. musí mít správnou délku
    3. nesmí začínat nulou ale může ji obsahovat
    4. musí obsahovat pouze číslice
    5. má unikátní číslice (nesmí se opakovat).
    """
    chyby = []
    if not cislo:
        chyby.append("Nebylo nic zadáno!")
    else:
        if len(cislo) != POCET_CIFER:
            chyby.append("Délka není správná!")
        if cislo[0] == "0":
            chyby.append("Číslo nesmí začínat nulou!")
        if not cislo.isdigit():
            chyby.append("Číslo může obsahovat pouze číslice!")
        if cislo.isdigit() and len(cislo) != len(set(cislo)):
            chyby.append("Číslice v čísle se nesmí opakovat!")    
    
    return chyby


def bulls(a: str, b: str) -> int:
    """
    Zjistí počet uhodnutých bulls.
    """
    pocet = 0
    for x, y in zip(a, b):
        if x == y:
            pocet += 1

    return pocet


def cows(a: str, b: str) -> int:
    """
    Zjistí počet uhodnutých cows.
    """
    pocet = len(set(a) & set(b))

    return pocet


# Délka oddělovače odpovídá nejdelšímu vypisovanému textu.
ODDELOVAC = "-" * 55
# Stanovení počtu cifer pro náhodné a zadané číslo.
POCET_CIFER = 4
# Povolené číslice pro generování náhodného čísla.
CISLICE = "0123456789"

def main():
    print(f"""
{ODDELOVAC}
Ahoj!
{ODDELOVAC}
Vygeneroval jsem pro tebe náhodné {POCET_CIFER}-ciferné číslo.
Pojď si zahrát hru \"Bulls&Cows\".
{ODDELOVAC}""")

    nahodne_cislo = vytvor_cislo()
    pokus = 0

    while True:
        if pokus == 0:
            print(f"Zadej {POCET_CIFER}-ciferné číslo:")
            print(f"{ODDELOVAC}")
        pokus += 1
        zadane_cislo = input(">>>")
        chyby_cisla = "\n".join(over_cislo(zadane_cislo))
        if not chyby_cisla:
            pocet_bulls = bulls(nahodne_cislo, zadane_cislo)
            pocet_cows = cows(nahodne_cislo, zadane_cislo) - pocet_bulls
            text_bull = "bull" if pocet_bulls == 1 else "bulls"
            text_cow = "cow" if pocet_cows == 1 else "cows"
            if pocet_bulls == POCET_CIFER:
                print(f"Gratuluji! Náhodné číslo bylo odhaleno.")
                print(f"Počet pokusů: {pokus}")
                print(f"{ODDELOVAC}")
                break
            else:
                print(f"{pocet_bulls} {text_bull}, {pocet_cows} {text_cow}")
                print(f"{ODDELOVAC}")
        else:
            print(f"{chyby_cisla}")
            print(f"{ODDELOVAC}")
            print(f"Zkus to znova:")
            print(f"{ODDELOVAC}")


if __name__ == "__main__":
    main()