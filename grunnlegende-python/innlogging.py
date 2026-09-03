import bcrypt
from getpass import getpass

users: dict[str,bytes] = {
    # username:password
    "Bruker1": bcrypt.hashpw(b"passord1", bcrypt.gensalt()), 
    "Bruker2": bcrypt.hashpw(b"aaaaaaaaaa", bcrypt.gensalt()), 
    "benjamin": bcrypt.hashpw(b"chinese", bcrypt.gensalt()),
}

currentUser: str | None = None

def login(username:str, password: str) -> bool:
    global currentUser

    hashed_password: bytes | None = users.get(username)

    if hashed_password == None:
        return False

    if bcrypt.checkpw(password.encode("utf-8"),hashed_password):
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