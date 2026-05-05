
from getpass import getpass
import json

import typer
import remotefuncs
from remotefuncs import sha, baseify, attr, encrypt, get, byte, inpute, getepass
app = typer.Typer()
add = typer.Typer()
remove = typer.Typer()
app.add_typer(remove, name="remove")
app.add_typer(add, name="add")
add.add_typer(add, name="remove")
@add.command("user")
def add_user():
    username = inpute("Username for new user: ")
    password = getepass()
    combohash = baseify(sha(username + password)).decode()
    print("User added successfully.")
    data= {
        "combohash": combohash
    }
    with open(baseify(sha(username)), "w") as f:
        json.dump(data, f, indent=4)
@remove.command("user")
def remove_user():
    username = inpute("Username to remove: ")
    password = getepass()
    combohash = baseify(sha(username + password)).decode()
    try:
        with open(baseify(sha(username)), "r") as f:
            data = json.load(f)
            if data.get("combohash") == combohash:
                import os
                os.remove(baseify(sha(username)))
                print("User removed successfully.")
            else:
                print("Incorrect username or password.")
    except FileNotFoundError:
        print("User not found.")
if __name__ == "__main__":
    app()