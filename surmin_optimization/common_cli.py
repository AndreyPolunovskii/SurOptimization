from surmin_optimization.example.SurMinTest import main
import typer

common_cli: typer.Typer = typer.Typer()




@common_cli.command()
def solve() -> None:
    main()


