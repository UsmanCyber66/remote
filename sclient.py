
from getpass import getpass
import json

import typer
import remotefuncs
from remotefuncs import sha, baseify, attr, encrypt, get, byte, inpute, getepass
app = typer.Typer()


add= typer.Typer()
app.add_typer(add, name="add")

@add.command()
def user():
    username = inpute("Username for new user: ")
    password = getepass()
    combohash = baseify(sha(username + password)).decode()
    print("User added successfully.")
    data= {
        "combohash": combohash
    }
    with open(baseify(sha(username)), "w") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    app()