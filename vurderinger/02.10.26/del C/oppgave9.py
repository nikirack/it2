"""
Oppgave 9: Varebeholdning i en nettbutikk (9 poeng)
Du skal lage et enkelt lagersystem for en liten nettbutikk som selger datautstyr. For hver vare må butikken holde styr på:

et varenummer (unikt for hver vare, for eksempel "A100")
navn
pris
antall på lager
kategori (for eksempel "tastatur", "mus" eller "skjerm")
a) Lag en passende datastruktur for lageret, og fyll den med minst fem varer. Noen av varene skal ha få (under 5) eller ingen på lager. Skriv en kommentar som forklarer hvorfor du valgte akkurat denne strukturen. (2 poeng)

b) Lag en funksjon vis_lager(lager) som skriver ut alle varene som en ryddig tabell, med prisen med to desimaler. Kolonnene skal stå pent under hverandre. (2 poeng)

c) Lag en funksjon selg_vare(lager, varenummer, antall) som: (3 poeng)

skriver ut en feilmelding og returnerer False hvis varenummeret ikke finnes
skriver ut en feilmelding og returnerer False hvis det ikke er nok varer på lager
ellers trekker antallet fra lagerbeholdningen, skriver ut hva kunden må betale, og returnerer True
Vis at funksjonen fungerer ved å kalle den minst tre ganger: ett salg som går bra, ett med ukjent varenummer og ett der det er for få på lager.

d) Lag en funksjon lav_beholdning(lager, grense=5) som returnerer en liste med navnene på alle varer som har færre enn grense på lager, sortert slik at varen med minst på lager kommer først. Skriv ut resultatet. (2 poeng)
"""

from typing import TypedDict

# a) datastruktur
class Vare(TypedDict):
    name: str
    pris: float
    antall_på_lager: int
    kategori: str

tabel: dict[str,Vare] = {
    "A100":{"name":"ps1", "pris":1000,"antall_på_lager":0,"kategori":"spill konsoll"},
    "A400":{"name":"ps4", "pris":3000,"antall_på_lager":11,"kategori":"spill konsoll"},
    "B12":{"name":"lader", "pris":199.99,"antall_på_lager":52,"kategori":"tilbehør"},
    "B99":{"name":"ps4 kontroller", "pris":599.99,"antall_på_lager":12,"kategori":"tilbehør"},
    "I13":{"name":"Iphone 13", "pris":9000,"antall_på_lager":3,"kategori":"telefon"},
}
# Jeg bruker dict fordi det er det jeg syntes er best for å lagre data på en måte jeg kan lett hente ut fra, jeg brukte varenummeret som primary key
# Jeg brukte også noe som heter TypedDict fordi det gir meg bedre hjelp i vscode når jeg skrive noe reletert til den dicten.
 
# b)

def vis_lager(lager: dict[str, Vare]) -> None:
    for vareNummer, vare in lager.items():
        print(f"Vare nummer: {vareNummer:8} Navn: {vare['name']:15} Pris: {f"{vare['pris']:.2f}":8} antall på lager: {vare['antall_på_lager']:3} kategori: {vare['kategori']:10}")

vis_lager(tabel)

# c) 
def selg_vare(lager: dict[str, Vare], varenummer:str, antall:int) -> bool:
    try:
        vare = lager[varenummer]
        if vare["antall_på_lager"] - antall >= 0:
            vare["antall_på_lager"] -= antall
            return True
        else:
            print(f"Det er ikke nokk varer i gjenn for å selge {antall}")
            return False
    except:
        print(f"Varen {varenummer} eksisterer ikke")
        return False

print(selg_vare(tabel,"A100",1))
print(selg_vare(tabel,"B12",10))
print(selg_vare(tabel,"A67",1))
vis_lager(tabel)

# d)
def lav_beholdning(lager:dict[str, Vare], grense:int=5) -> list[str]:
    varer: list[str] = []
    for _, vare in lager.items():
        if vare["antall_på_lager"] < grense:
            varer.append(vare["name"])

    return varer

print(lav_beholdning(tabel))