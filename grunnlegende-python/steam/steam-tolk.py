import json
from typing import TypedDict
from pathlib import Path

class Game(TypedDict):
    appid: int
    name: str
    playtime_forever: int
    img_icon_url: str
    # playtime_windows_forever: int
    # playtime_mac_forever: int
    # playtime_linux_forever: int
    # playtime_deck_forever: int
    rtime_last_played: int
    content_descriptorids: list[int]
    playtime_disconnected: int
    playtime_forever_hours: int
    playtime_2weeks: int

class GameList(TypedDict):
    game_count: int
    games: list[Game]



GAMES_PATH: Path = Path(__file__).parent / "games.json"

with open(GAMES_PATH, "r", encoding="utf-8") as f:
    games: GameList = json.load(f)


def max_playtime(games:GameList) -> Game:
    max_playtime: dict[str,int] = {
        "playtime":0,
        "game":0
    }
    for i, game in enumerate(games["games"]):
        if game["playtime_forever"] > max_playtime["playtime"]:
            max_playtime["playtime"] = game["playtime_forever"]
            max_playtime["game"] = i
    return(games["games"][max_playtime["game"]])



def main() -> None:
    print(len(games["games"]))
    print(f"Game: {max_playtime(games)['name']}, Playtime {max_playtime(games)['playtime_forever_hours']} hours")



if __name__ == "__main__":
    main()