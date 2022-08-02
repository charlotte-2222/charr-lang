import logging
import typing as t

import sly

from lexer import CharrLexer
from models import Module
from parser import CharrParser

""" This is the main compiler class. 
It is responsible for taking a Charr source file and compiling it to a binary file. 
It is also responsible for taking a binary file and executing it. """


class CompilerToken:
    # This is the token type for the compiler.
    # It is used to determine what type of token is being used.
    # i.e. if the token is a keyword, a number, a string, etc.
    # This is used to determine what type of action to take when parsing the token.
    def __init__(self,
                 original_token: sly.lex.Token,
                 source: str) -> None:
        self.original_token = original_token
        self.source = source

    def __repr__(self) -> str:
        return repr(f"{self.original_token}")

    @property
    def value(self) -> str:
        return self.original_token.value

    @property
    def type(self) -> str:
        return self.original_token.type

    @property
    def lineno(self) -> int:
        return self.original_token.lineno

    @property
    def index(self) -> int:
        return self.original_token.index

    @property
    def lineco(self) -> int:
        last_line_break = max(self.source.rfind("\n", 0, self.original_token.index), 0)
        return token.index - last_line_break + 1


class CharrCompiler:
    """compiler.py:"""
    # This is the main function for the compiler.
    # It takes a Charr source file and compiles it to a binary file.
    # It is also responsible for taking a binary file and executing it.

    def __init__(self):
        self.lexer = CharrLexer()
        self.parser = CharrParser()

    def tokens(self, source: str) -> t.Generator[CompilerToken, None, None]:
        for token in self.lexer.tokenize(source):
            self.lexer.log.debug("Encounterd token, %r" % token)
            yield CompilerToken(token, source)

    def compile(self, source: str, level: int = 0) -> Module:
        logging.basicConfig(
            format="[%(name)s] %(levelname)s: %(message)s",
            level=level
        )
        return self.parse(source)

    def parse(self, source: str) -> Module:
        self.parser.log.flush()
        return self.parser.parse(self.tokens(source))
