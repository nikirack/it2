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

while True:
    while True:
        print("Skriv et av alternativene")
        for i, valg in enumerate(alternativ, 1):
            print(f"{i}. {valg}")
        bruker_valg_tall = int(input("Velg (1-3): "))
        
        if bruker_valg_tall in range(1,len(alternativ)+1):
            break
        print("Ugyldig valg")

    bruker_valg: str = alternativ[bruker_valg_tall-1]

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