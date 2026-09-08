# import random
# winning: dict[str,str] = {"stein":"saks","saks":"papir","papir":"stein"}
# for _ in range(3): 
#     user = input("stein, saks eller papir: ")
#     bot = random.choice(["stein","saks","papir"])
#     if winning[user] == bot: print("bruker vant")
#     elif user == bot: print("uavgjort")
#     else: print("bot vant")

# import random 
# winning: dict[str,str] = {"stein":"saks","saks":"papir","papir":"stein"}
# for _ in range(3): 
#     user = input("stein, saks eller papir: ")
#     bot = random.choice(["stein","saks","papir"])
#     print("bruker vant" if winning[user] == bot else "uavgjort" if user == bot else "bot vant")

# import random; winning: dict[str,str] = {"stein":"saks","saks":"papir","papir":"stein"}
# for _ in range(3): user = input("stein, saks eller papir: "); bot = random.choice(["stein","saks","papir"]); print("bruker vant" if winning[user] == bot else "uavgjort" if user == bot else "bot vant")