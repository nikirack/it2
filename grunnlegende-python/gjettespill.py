import random

randnumber = random.randint(1,100)

won = False

while not won:
    user = int(input("Velg et tall: "))

    if user > randnumber:
        print("For høyt")
    elif user < randnumber:
        print("For lavt")
    else:
        won = True
        print("Du vant")
