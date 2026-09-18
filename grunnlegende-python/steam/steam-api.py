import requests
import json
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

STEAM_API_KEY: str | None = os.getenv("STEAM_API_KEY")
STEAM_ID64: str | None = os.getenv("STEAM_ID64")

OUTPUT_FILE: Path = Path(__file__).parent / "games.json"

def hentSteamSpill():
    url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"

    if (STEAM_API_KEY == None) or (STEAM_ID64 == None):
        print("api key eller id er ikke definert")
        return

    params: dict[str,str] = {
        "key":STEAM_API_KEY,
        "steamid":STEAM_ID64,
        "format":"json",
        "include_appinfo":"true",
        "include_played_free_games":"true",
    }

    print("Henter spilldata fra Steam...")

    response: requests.Response = requests.get(url=url, params=params)

    print(response)

    if response.ok:
        data = response.json().get("response")

        for game in data["games"]:
            playtime_forever_hours = int(game["playtime_forever"] / 60)

            game["playtime_forever_hours"] = playtime_forever_hours
            if game.get("playtime_2weeks") is None:
                game["playtime_2weeks"] = 0

        with open(OUTPUT_FILE, "w") as f:
            json.dump(data,f, indent=4)

    else:
        print("error getting response")
        print(response.status_code)
        print(response.text)

hentSteamSpill()
