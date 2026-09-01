import random

alternativ: list[str] = ["stein", "saks", "papir"]

winning: dict[str,str] = {
    "stein": "saks",
    "saks": "papir",
    "papir": "stein",
}

score: dict[str, int] = {
    "bruker": 0,
    "data": 0,
    "uavgjort": 0,
}

def hent_brukervalg() -> str:
    while True:
            print("Skriv et av alternativene")
            for i, valg in enumerate(alternativ, 1):
                print(f"{i}. {valg}")
    
            try:
                bruker_valg_tall = int(input("Velg (1-3): "))
    
                if  1 <= bruker_valg_tall <= len(alternativ):
                    break
                print("Ugyldig valg")
            except ValueError:
                print("Please enter a valid number")
    
    bruker_valg: str = alternativ[bruker_valg_tall-1]

    return bruker_valg
    
while True:
    bruker_valg: str = hent_brukervalg()

    data_valg: str = random.choice(alternativ)

    if winning[bruker_valg] == data_valg:
        print("du vant")
        score["bruker"] += 1
    elif bruker_valg == data_valg:
        print("uavgjort")
        score["uavgjort"] += 1
    else:
        print("du tapte")
        score["data"] += 1

    print(score)

    if input("spille igjen (Y/n)").lower() == "n":
        break

print("Final score:")
print(score)