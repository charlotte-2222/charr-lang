import io
import logging

import click

from compiler import CharrCompiler

compiler = CharrCompiler()

"""This is a part of the compiler."""


@click.group()
# Will be used to create the CLI for the compiler.
def cli():
    """
    Welcome to the Charr Language! This is a compiler for the Charr language.
    """


@cli.command(name="compile")
@click.argument("file", type=click.File("r"), default="main.charr")
@click.option("-l", "--level", default="ERROR", help="Logging level: (DEBUG, INFO, WARNING, ERROR, CRITICAL)")
# Provides the CLI for the compiler.
# Options:
# -l, --level: The logging level.
def cli_compile(file: io.TextIOWrapper, level: str):
    """compiles a new charr file to binary"""
    compiler.compile(file.read(), level=getattr(logging, level.upper()))


@cli.command(name="interactive")
# Interactive CLI for the compiler.
# This is used to run the compiler in an interactive mode.
def cli_interactive(verbose: int):
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
    # This is the main function for the cli / compiler.
    cli()
