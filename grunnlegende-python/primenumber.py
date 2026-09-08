import math

num: int = int(input("Skriv in et tall: "))

is_prime: bool = True

for i in range(2, int(math.sqrt(num))):
    if (num % i == 0):
        is_prime = False
        print("Tallet er ikke et primtall")
        break
if is_prime:
    print("Tallet er et primtall")
