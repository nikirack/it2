from getpass import getpass

users: dict[str,str] = {
    # username:password
    "Bruker1":"passord1",
    "Bruker2":"aaaaaaaaaa",
    "benjamin":"chinese"
}

currentUser: str | None = None

def login(username:str, password: str) -> bool:
    global currentUser

    if users.get(username) == password:
        currentUser = username
        return True

    return False

while currentUser is None:
    username: str = input("Skriv brukernavnet ditt: ")
    password: str = getpass("Skriv passordet ditt: ", echo_char="*")

    if login(username,password):
        print(f"Du er logget in som {currentUser}")
        break
    else:
        print("Feil passord eller brukernavn")