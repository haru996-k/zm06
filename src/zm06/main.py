import datetime

import typer

from . import mathtools

from . import demo

from . import baseball


app = typer.Typer()


@app.callback()
def callback():
    """
    A Collection of Useful Commands
    """


@app.command()
def now():
    """
    Show local date and time
    """
    today = datetime.datetime.today()
    typer.echo(today.strftime('%A, %B %d, %Y'))


@app.command()
def gcd(x: int, y: int):
    """
    Greatest Common Divisor
    """
    typer.echo(mathtools.gcd(x, y))


@app.command()
def lcm(x: int, y: int):
    """
    Least Common Denominator
    """
    typer.echo(mathtools.lcm(x, y))


@app.command()
def num_perfect(n: int):
    """
    Check Perfect Number
    """
    typer.echo(mathtools.num_perfect(n))

@app.command()
def hello(name: str = "Haruto"):
    typer.echo(demo.hello(name))

@app.command()
def baseball_score():
    """
    NPBの現在のスコアを表示
    """
    typer.echo(baseball.npb_scores())

if __name__ == "__main__":
    app()
