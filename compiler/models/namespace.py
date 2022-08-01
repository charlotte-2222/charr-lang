from .base import Ast

class Namespace(Ast):
    name: str
    ctx: str