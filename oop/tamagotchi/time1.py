# ikke OOP

# Del A
# from typing import Callable, TypedDict

# class Kjæledyr(TypedDict):
#     navn: str
#     sult: int
#     energi: int
#     glede: int

# frido: Kjæledyr = {"navn":"Fido", "sult":0, "energi":10, "glede":10}

# def begrens(verdi: int) -> int:
#     return max(0, min(10, verdi))

# def Mate(kjæledyr: Kjæledyr) -> None:
#     kjæledyr["sult"] = begrens(kjæledyr["sult"]-3)
#     kjæledyr["glede"] = begrens(kjæledyr["glede"]+1)

#     TidenGår(kjæledyr)

# def Leke(kjæledyr: Kjæledyr) -> None:
#     if kjæledyr["energi"] >= 2:
#         kjæledyr["glede"] = begrens(kjæledyr["glede"]+3)
#         kjæledyr["energi"] = begrens(kjæledyr["energi"]-2)
#         kjæledyr["sult"] = begrens(kjæledyr["sult"]+1)

#     else:
#         print(f"Du kan kun leke når {kjæledyr['navn']} sin energi er mer en 1")

#     TidenGår(kjæledyr)
    
# def Sove(kjæledyr: Kjæledyr) -> None:
#     kjæledyr["energi"] = begrens(kjæledyr["energi"]+4)
#     kjæledyr["sult"] = begrens(kjæledyr["sult"]-1)

#     TidenGår(kjæledyr)

# def Avslutt() -> None:
#     global avsluttet
#     avsluttet = True


# def TidenGår(kjæledyr: Kjæledyr) -> None:
#     kjæledyr["glede"] = begrens(kjæledyr["glede"]-1)
#     kjæledyr["sult"] = begrens(kjæledyr["sult"]+1)

# def Vis(kjæledyr: Kjæledyr) -> None:
#     print(f"{kjæledyr['navn']}: sult {kjæledyr['sult']}, energi {kjæledyr['energi']}, glede {kjæledyr['glede']}")

# alternativer: dict[int, Callable[[Kjæledyr], None]] = {
#     1:Mate,
#     2:Leke,
#     3:Sove,
#     0:Avslutt, # type: ignore
# }

# def meny() -> None:
#     Vis(frido)
#     print("1: Mate  2: Leke  3: Sove  0: Avslutt")
#     try:
#         valg = int(input("Velg: "))
#         alternativer[valg](frido)
#     except:
#         print("Du må velge et av alternativene.")


# avsluttet = False

# while not avsluttet:
#     meny()




# Del B
# from typing import Callable, TypedDict

# class Kjæledyr(TypedDict):
#     navn: str
#     sult: int
#     energi: int
#     glede: int

# Frido: Kjæledyr = {"navn":"Fido", "sult":0, "energi":10, "glede":10}
# Pusur: Kjæledyr = {"navn":"Pusur", "sult":0, "energi":10, "glede":10}

# def begrens(verdi: int) -> int:
#     return max(0, min(10, verdi))

# def Mate(kjæledyr: Kjæledyr) -> None:
#     kjæledyr["sult"] = begrens(kjæledyr["sult"]-3)
#     kjæledyr["glede"] = begrens(kjæledyr["glede"]+1)

#     TidenGår(kjæledyr)

# def Leke(kjæledyr: Kjæledyr) -> None:
#     if kjæledyr["energi"] >= 2:
#         kjæledyr["glede"] = begrens(kjæledyr["glede"]+3)
#         kjæledyr["energi"] = begrens(kjæledyr["energi"]-2)
#         kjæledyr["sult"] = begrens(kjæledyr["sult"]+1)

#     else:
#         print(f"Du kan kun leke når {kjæledyr['navn']} sin energi er mer en 1")

#     TidenGår(kjæledyr)
    
# def Sove(kjæledyr: Kjæledyr) -> None:
#     kjæledyr["energi"] = begrens(kjæledyr["energi"]+4)
#     kjæledyr["sult"] = begrens(kjæledyr["sult"]-1)

#     TidenGår(kjæledyr)

# def Avslutt() -> None:
#     global avsluttet
#     avsluttet = True


# def TidenGår(kjæledyr: Kjæledyr) -> None:
#     kjæledyr["glede"] = begrens(kjæledyr["glede"]-1)
#     kjæledyr["sult"] = begrens(kjæledyr["sult"]+1)

# def Vis(kjæledyr: Kjæledyr) -> None:
#     print(f"{kjæledyr['navn']}: sult {kjæledyr['sult']}, energi {kjæledyr['energi']}, glede {kjæledyr['glede']}")

# alternativer: dict[int, Callable[[Kjæledyr], None]] = {
#     1:Mate,
#     2:Leke,
#     3:Sove,
#     0:Avslutt, # type: ignore
# }

# def meny() -> None:
#     Vis(Frido)
#     Vis(Pusur)

#     print("1: Frido, 2: Pusur")
#     dyr = int(input("Velg: "))

#     print("1: Mate  2: Leke  3: Sove  0: Avslutt")
#     try:
#         valg = int(input("Velg: "))
#         if dyr == 1:
#             alternativer[valg](Frido)
#         elif dyr == 2:
#             alternativer[valg](Frido)
#         else:
#             print("Du må velge enten Frido eller Pusur")
#     except:
#         print("Du må velge et av alternativene.")


# avsluttet = False

# while not avsluttet:
#     meny()



# Del C
from typing import Callable, TypedDict

class Kjæledyr(TypedDict):
    navn: str
    sult: int
    energi: int
    glede: int

Dyr: list[Kjæledyr] = [
    {"navn":"Fido", "sult":5, "energi":5, "glede":5},
    {"navn":"Pusur", "sult":5, "energi":5, "glede":5}
]

def begrens(verdi: int) -> int:
    return max(0, min(10, verdi))

def Mate(kjæledyr: Kjæledyr) -> None:
    kjæledyr["sult"] = begrens(kjæledyr["sult"]-3)
    kjæledyr["glede"] = begrens(kjæledyr["glede"]+1)

    TidenGår(kjæledyr)

def Leke(kjæledyr: Kjæledyr) -> None:
    if kjæledyr["energi"] >= 2:
        kjæledyr["glede"] = begrens(kjæledyr["glede"]+3)
        kjæledyr["energi"] = begrens(kjæledyr["energi"]-2)
        kjæledyr["sult"] = begrens(kjæledyr["sult"]+1)

    else:
        print(f"Du kan kun leke når {kjæledyr['navn']} sin energi er mer en 1")

    TidenGår(kjæledyr)
    
def Sove(kjæledyr: Kjæledyr) -> None:
    kjæledyr["energi"] = begrens(kjæledyr["energi"]+4)
    kjæledyr["sult"] = begrens(kjæledyr["sult"]-1)

    TidenGår(kjæledyr)

def Adopter(navn:str) -> None:
    Dyr.append({"navn":navn, "sult":5, "energi":5, "glede":5})

def Avslutt() -> None:
    global avsluttet
    avsluttet = True


def TidenGår(kjæledyr: Kjæledyr) -> None:
    kjæledyr["glede"] = begrens(kjæledyr["glede"]-1)
    kjæledyr["sult"] = begrens(kjæledyr["sult"]+1)

def Vis(kjæledyr: Kjæledyr) -> None:
    print(f"{kjæledyr['navn']}: sult {kjæledyr['sult']}, energi {kjæledyr['energi']}, glede {kjæledyr['glede']}")

alternativer: dict[int, Callable[[Kjæledyr], None]] = {
    1:Mate,
    2:Leke,
    3:Sove,
}

def meny() -> None:
    for dyr in Dyr:
        Vis(dyr)
        
    print("1: Mate  2: Leke  3: Sove 4: Adopter nytt dyr  0: Avslutt")

    try:
        valg = int(input("Velg: "))
        if valg == 4:
            navn: str = input("Hva skal kjæledyret hete?: ")
            Adopter(navn)
        elif valg == 0:
            Avslutt()
        else:
            for index, dyr in enumerate(Dyr,1):
                print(f"{index}: {dyr['navn']}, ", end="")
                print()

            navn: str = input("Hvilke dyr skal gjøre dette?: ")
            alternativer[valg](Dyr[navn-1])
    except:
        print("Du må velge et av alternativene.")


avsluttet = False

while not avsluttet:
    meny()