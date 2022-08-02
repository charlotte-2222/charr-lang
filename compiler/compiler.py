import logging
import typing as t

import sly

from lexer import CharrLexer
from models import Module
from parser import CharrParser


class CompilerToken:
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


