
import typer
import remotefuncs
app = typer.Typer()


add= typer.Typer()
app.add_typer(add, name="add")

@add.command()
def user():
    

if __name__ == "__main__":
    app()