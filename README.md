Elections Scraper
-----------------
Třetí projekt Python akademie od Engeta.

Popis projektu
--------------
Tento projekt stahuje a ukládá výsledky parlamentních voleb v roce 2017. 
Odkaz na webovou stránku: https://volby.gov.cz/pls/ps2017nss/ps3?xjazyk=CZ

Instalace knihoven
------------------
Knihovny, které jsou nezbytné ke správnému fungování  jsou uloženy v souboru requirements.txt. Pro instalaci
si vytvořte a aktivujte nové virtuální prostředí. Následně v terminálu spusťte příkaz:

pip install -r requirements.txt

Spuštění
--------
Spuštění probíhá v příkazovém řádku za pomocí dvou argumentů:
1. url územního celku ve sloupečku "Výběr obce", který chcete stáhnout
2. název souboru, do kterého se mají data uložit.

Vzor: python main.py "odkaz-uzemniho-celku" "vysledny-soubor"   

Vzorová ukázka
--------------
Výsledky voleb pro okres: Ústí nad Labem

url: https://volby.gov.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=6&xnumnuts=4207
název souboru: Ústí nad Labem.csv

Spuštění:
python main.py "https://volby.gov.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=6&xnumnuts=4207" "Ústí nad Labem.csv"


Průběh stahování:

Stahuji data ze zadaného url: https://volby.gov.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=6&xnumnuts=4207
Ukládám data do souboru: Ústí nad Labem.csv
Data úspěšně stažena a uložena.

Ukázka výstupu:

kod obce;název obce;voliči v seznamu;vydané obálky;platné hlasy;Občanská demokratic...... 
567931;Dolní Zálezly;462;316;314;39;0;0;14;21;35;4;1;2;0;3;28;0;14;102;0;0;6;0;2;1;1;36;5
567957;Habrovany;182;101;100;5;0;0;4;2;19;0;0;3;2;0;1;0;2;42;0;1;2;0;1;1;1;14;0
......