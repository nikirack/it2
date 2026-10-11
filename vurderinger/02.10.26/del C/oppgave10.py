from typing import Callable, TypedDict

class Økt(TypedDict):
    aktivitet: str
    antall_min: int

økter: dict[int, Økt] = {}
current = 1

avsluttet = False

def registrer() -> None:
    global current
    aktivitet: str = input("Hvilke aktivitet gjorde du?: ")
    try:
        antall_min = int(input("Hvor mange minutter gjorde du aktiviteten?: "))
        økter[current] = {"aktivitet":aktivitet, "antall_min":antall_min}
        current+=1
    except:
        print("antall minutter må være et tall.")

def vis() -> None:
    print("")
    for nummer, økt in økter.items():
        print(f"{nummer}. {økt['aktivitet']}: {økt['antall_min']} min")
    print("")

def statistikk() -> None:
    print("--- Statistikk ---")
    print(f"Antall økter: {len(økter)}")

    class Stat(TypedDict):
        antall_økter: int
        total_min:int

    stat: dict[str,Stat] = {}
    
    for _, økt in økter.items():
        try:
            existerer = stat[økt["aktivitet"]]
            stat[økt["aktivitet"]] = {"antall_økter":existerer["antall_økter"]+1,"total_min":existerer["total_min"]+økt["antall_min"]}
        except:
            stat[økt["aktivitet"]] = {"antall_økter":1,"total_min":økt["antall_min"]}
    print(stat)
    # Fikk ikke tid til å få statistikken til å se fin ut


def avslutt() -> None:
    global avsluttet
    avsluttet = True

alternativer: dict[int, Callable[[], None]] = {
    1:registrer,
    2:vis,
    3:statistikk,
    4:avslutt
    }

def meny() -> None:
    print("--- Treningslogg ---")
    print("1: Registrer økt")
    print("2: Vis alle økter")
    print("3: Statistikk")
    print("4: Avslutt")
    try:
        valg = int(input("Velg: "))
        if valg in range(1,4+1):
            alternativer[valg]()
        else:
            print("Velg en av alternativene.")
    except:
        print("Du må skrive et tall.")



while not avsluttet:
    meny()