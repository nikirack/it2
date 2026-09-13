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


# _ = [
#     globals().update({"random":__import__("random"),"winning":{"stein":"saks","saks":"papir","papir":"stein"}}),
#     [(
#         globals().update({"user": input("stein, saks eller papir: ")}),
#         globals().update({"bot": random.choice(["stein", "saks", "papir"])}),
#         print(
#             "bruker vant" if winning[user] == bot
#             else "uavgjort" if user == bot
#             else "bot vant"
#         )
#     )
#     for _ in range(3)]
# ]

# one line no semicolon 
_ = [ globals().update({"random":__import__("random"),"winning":{"stein":"saks","saks":"papir","papir":"stein"}}), [( globals().update({"user": input("stein, saks eller papir: ")}), globals().update({"bot": random.choice(["stein", "saks", "papir"])}), print( "bruker vant" if winning[user] == bot else "uavgjort" if user == bot else "bot vant" )) for _ in range(3)]]