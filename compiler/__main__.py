import io
import logging

import click

from compiler import CharrCompiler

compiler = CharrCompiler()


@click.group()
def cli():
    """
    Welcome to the Charr Language! This is a compiler for the Charr language.
    """


@cli.command(name="compile")
@click.argument("file", type=click.File("r"), default="C:\\Users\\ayych\\PycharmProjects\\pyLanguage\\main.chr")
@click.option("-l", "--level", default="ERROR",
              help="Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL), see logging module")
def cli_compile(file: io.TextIOWrapper, level: str):
    """compiles a new charr file to binary"""
    compiler.compile(file.read(), level=getattr(logging, level.upper()))


@cli.command(name="interactive")
def cli_interactive(verbose: bool = False):
    """interactive mode"""
    code = ""
    click.echo("Charr Interactive Mode")
    while True:
        line = input(": ")
        if line.strip() == "":
            break
        code += line + "\n"
    click.echo(compiler.compile(code, level=getattr(logging, level.upper())))


if __name__ == "__main__":
    cli()
