import os, subprocess
import time

def begrens(verdi: int) -> int:
    return max(0, min(10, verdi))

class Kjaeledyr:
    def __init__(self, navn:str) -> None:
        self.navn: str = navn
        self.sult: int = 5
        self.energi: int = 5
        self.glede: int = 5

    def vis(self) -> None:
        print(f"{self.navn}: sult {self.sult}, energi {self.energi}, glede {self.glede}")

    def begrens_alle(self) -> None:
        self.sult = begrens(self.sult)
        self.energi = begrens(self.energi)
        self.glede = begrens(self.glede)

    def mate(self) -> None:
        self.sult -= 3
        self.glede += 1

        self.begrens_alle()

        print(f"Du ga {self.navn} mat.")

    def leke(self) -> None:
        if self.energi < 2:
            print(f"{self.navn} er for trøtt til å leke.")
            return
        self.glede += 3
        self.energi -= 2
        self.sult += 1

        self.begrens_alle()

        print(f"Du lekte med {self.navn}.")

    def sove(self) -> None:
        self.energi += 4
        self.sult -= 1
        
        self.begrens_alle()

        print(f"{self.navn} sov godt.")

    def tiden_gaar(self) -> None:
        self.sult += 1
        self.glede -= 1

        self.begrens_alle()

dyrene: list[Kjaeledyr] = [Kjaeledyr("Fido"), Kjaeledyr("Pusur")]

def velg_dyr(dyrene: list[Kjaeledyr]) -> Kjaeledyr | None:
    for index, dyr in enumerate(dyrene, 1):
        print(f"{index}: {dyr.navn}")
    
    try:
        return dyrene[int(input("Hvilket dyr? ")) - 1]
    except (ValueError, IndexError):
        print("Ugyldig dyr.")
        return None

def clear_terminal() -> None:
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


while True:
    clear_terminal()

    for dyr in dyrene:
        dyr.vis()

    print("1: Mate  2: Leke  3: Sove  4: Adopter nytt dyr  0: Avslutt")
        
    valg = int(input("Velg: "))

    if valg == 0:
        break
    elif valg == 4:
        dyrene.append(Kjaeledyr(input("Navn på dyret: ")))
    else:
        print()

        dyr: Kjaeledyr | None = velg_dyr(dyrene)

        if dyr == None:
            print("\nUgyldig valg.")
            time.sleep(2)
            continue

        match valg:
            case 1:
                dyr.mate()
            case 2:
                dyr.leke()
            case 3:
                dyr.sove()
            case _:
                print("\nUgyldig valg.")
                time.sleep(2)
                continue

        time.sleep(2)

    for dyr in dyrene:
        dyr.tiden_gaar()