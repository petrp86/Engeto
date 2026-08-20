import sys
from urllib.parse import urljoin
import csv

import requests
from bs4 import BeautifulSoup as bs


def main():
    url, nazev_souboru = overeni_argumentu()
    rozdelena_stranka, radky_tabulek = stazeni_rozdeleni_radky(url)
    rozliseni_stranky(rozdelena_stranka)
    print(f"Stahuji data ze zadaného url: {url}")
    seznam_vysledku = ulozeni_dat_obci(radky_tabulek, url)
    for klic in seznam_vysledku:
        url_s_vysledky = seznam_vysledku[klic].pop("adresa")
        _, radky_s_vysledky = stazeni_rozdeleni_radky(url_s_vysledky)
        vysledky_celkove = ulozeni_vysledku(radky_s_vysledky)
        seznam_vysledku[klic].update(vysledky_celkove)
    print(f"Ukládám data do souboru: {nazev_souboru}")
    ulozeni_do_csv(nazev_souboru, seznam_vysledku)
    print("Data úspěšně stažena a uložena.")


def overeni_argumentu() -> tuple:
    """
    Funkce ověřuje počet argumentů, jejich prohození a správnost.
    Vrací tupl zadané url a názvu souboru.
    """
    if len(sys.argv) != 3:
        print("Nebyl zadán správný počet argumentů.")
        sys.exit(1)
    url = sys.argv[1]
    nazev_souboru = sys.argv[2]
    if (url.lower().endswith(".csv") and 
        nazev_souboru.lower().startswith("https")):
        print("Argumenty jsou zadány v opačném pořadí.")
        sys.exit(1)
    overeni_url(url)
    overeni_nazvu_souboru(nazev_souboru)
    return url, nazev_souboru


def overeni_url(url: str):
    """
    Funkce testuje splnění podmínek pro zadání prvního argumentu.
    """
    if not url.startswith("https://"):
        print("Adresa url musí začínat \"https://...\".")
        sys.exit(1)
    if not url.startswith("https://volby.gov.cz/pls/ps2017"):
        print("Zadaná adresa není adresou výsledků parlamentních voleb 2017.")
        sys.exit(1)


def overeni_nazvu_souboru(nazev_souboru: str):
    """
    Funkce testuje splnění podmínek pro zadání druhého argumentu.
    """
    zakazane_znaky = "<>:\"/\\|?*"
    if not nazev_souboru.strip():
        print("Název souboru nesmí být prázdný.")
        sys.exit(1)
    if nazev_souboru != nazev_souboru.strip():
        print("Název souboru nesmí začínat/končit mezerou.")
        sys.exit(1)
    if nazev_souboru.lower().endswith(" .csv"):
        print("Název souboru nesmí obsahovat mezeru před příponou \".csv\".")
        sys.exit(1)
    if not nazev_souboru.lower().endswith(".csv"):
        print("Název souboru musí končit příponou \".csv\".")
        sys.exit(1)
    for znak in nazev_souboru:
        if znak in zakazane_znaky:
            print("Název souboru obsahuje nepovolené znaky.")
            sys.exit(1)


def stazeni_rozdeleni_radky(url: str) -> tuple:
    """
    Funkce uloží rozdělenou odpověď serveru pomocí BeautifulSoup 
    a uloží pouze řádky všech tabulek.
    Vrací tupl rozdělené stránky a řádky tabulek z ní.
    """
    stazena_stranka = odpoved_url(url)
    rozdelena_stranka = bs(stazena_stranka, "html.parser")
    radky_tabulek = rozdelena_stranka.find_all("tr")
    return rozdelena_stranka, radky_tabulek


def odpoved_url(url: str) -> str:
    """
    Funkce uloží a otestuje odpověď serveru zadané url.
    """
    try:
        odpoved = requests.get(url)
        if not odpoved.ok:
            print(f"Chyba při načítání stránky: "
                f"{odpoved.status_code} {odpoved.reason}")
            sys.exit(1)
    except requests.exceptions.RequestException:
        print("Vyskytla se neočekávaná chyba.")
        sys.exit(1)
    else:
        return odpoved.text


def rozliseni_stranky(rozdelena_stranka: bs):
    """
    Funkce ověřuje, jestli byla zadána url adresa "Výběr obce".
    """
    nadpis_h2 = rozdelena_stranka.find("h2").get_text(strip=True)
    if nadpis_h2 == ("Výsledky hlasování za územní celky – zvláštní "
        "volební okrsky"):
        print("Výsledky voleb pro Zahraničí nesplňují parametry pro "
            "stahování.")
        sys.exit(1)
    elif nadpis_h2 != ("Výsledky hlasování za územní celky – výběr obce"):
        print("Zadaná stránka voleb nesplňuje parametry pro stahování.\n"
            "Zadej odkaz ze sloupečku \"Výběr obce\".")
        sys.exit(1)


def ulozeni_dat_obci(radky_tabulek, url: str) -> dict:
    """
    Funkce vytváří slovník obsahující kód, název obce a odkaz na její 
    výsledky.
    """
    obce = {}
    for radek in radky_tabulek:
        try:
            kod = radek.find("td", class_="cislo").get_text(strip=True)
            bunky = radek.find_all("td")
            nazev = bunky[1].get_text(strip=True)
            url_odkaz = bunky[1].find("a")
            if url_odkaz:
                url_obce = urljoin(url, url_odkaz.get("href"))
                _, radky = stazeni_rozdeleni_radky(url_obce)
                vnorene_obce = ulozeni_dat_obci(radky, url_obce)
                obce.update(vnorene_obce)
            else:
                url_obce = urljoin(url, bunky[0].find("a").get("href"))
                obce[kod] = {"kód obce" : kod, "název obce" : nazev, "adresa" : url_obce,}
        except AttributeError:
            continue            
    return obce


def ulozeni_vysledku(radky_s_vysledky) -> dict:
    """
    Funkce vytváří slovník obsahují výsledky voleb pro jednu obec.
    """
    vysledky = {"voliči v seznamu" : radky_s_vysledky[2].find("td", 
                    headers="sa2").get_text(strip=True),
                "vydané obálky" : radky_s_vysledky[2].find("td", 
                    headers="sa3").get_text(strip=True),
                "platné hlasy" : radky_s_vysledky[2].find("td", 
                    headers="sa6").get_text(strip=True),}
    for radek in radky_s_vysledky[3:]:
        try:
            nazev_strany = radek.find("td", 
                class_="overflow_name").get_text(strip=True)
            bunky = radek.find_all("td")
            pocet_hlasu = bunky[2].get_text(strip=True)
        except AttributeError:
            continue
        else:
            vysledky[nazev_strany] = pocet_hlasu
    return vysledky


def ulozeni_do_csv(nazev_souboru: str, seznam_vysledku: dict):
    with open(nazev_souboru, mode="w", newline="") as soubor_csv:
        zapisovac = csv.DictWriter(soubor_csv,
            fieldnames=list(list(seznam_vysledku.values())[0].keys()),
            delimiter=";")
        zapisovac.writeheader()
        zapisovac.writerows(seznam_vysledku.values())


if __name__ == "__main__":
    main()