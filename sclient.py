
from getpass import getpass

import typer
import remotefuncs
from remotefuncs import sha, baseify, attr, encrypt, get, byte, inpute, getepass
app = typer.Typer()


add= typer.Typer()
app.add_typer(add, name="add")

@add.command()
def user():
    username = sha(inpute("Username for new user: "))
    password = getepass()
    
    print("User added successfully.") 

if __name__ == "__main__":
    app()