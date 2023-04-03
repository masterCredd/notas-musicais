
from rich.console import Console
from rich.table import Table
from typer import Argument, Typer

from notas_musicais.escalas import scale
from notas_musicais.acordes import wake_up


console = Console()
app = Typer()


@app.command()
def scales(
    tonic: str = Argument('c', help='Tônica da escala'),
    tonality: str = Argument('maior', help='Tonalidade da escala')
):
    table = Table()
    grades, degrees = scale(tonic, tonality).values()

    for degree in degrees:
        table.add_column(degree)
    table.add_row(*grades)
    
    console.print(table)
    
    
@app.command()
def chords(
    cipher: str = Argument('c', help='Cifra de um acorde')
):
    table = Table()
    grades, degrees = wake_up(cipher).values()

    for degree in degrees:
        table.add_column(degree)
    table.add_row(*grades)
    
    console.print(table)