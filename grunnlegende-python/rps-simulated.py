import random

choises: list[str] = ["stein", "saks", "papir"]

def get_random(times:int) -> dict[str, int]:
    stats: dict[str,int] = {
        "stein":0,
        "saks":0,
        "papir":0
    }

    for _ in range(times):
        stats[random.choice(choises)] += 1

    return stats


print(get_random(10_000))