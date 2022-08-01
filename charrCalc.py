"""
Starting a new language
----------------------
Name of lang: Charr (Sh sound)
Writer: Charlotte Childers, Generalist Software Developer (BanterAI)
Date Started: 8/1/2022
Programming Language: Python 3.10
"""

from sly import Lexer, Parser
from colorama import init, Fore, Back, Style

class CharrLexer(Lexer):
    tokens = {NAME, NUMBER, PLUS, TIMES, MINUS, DIVIDE, ASSIGN, LPAREN, RPAREN}
    ignore = ' \t'
    #literals = {'=', '+', '-', '*', '/', '(', ')', ',', ';', ':', '.'}

    # Tokens
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER = r'\d+'
    #STRING = r'\".*?\"'

    # Special symbols
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    ASSIGN = r'='
    LPAREN = r'\('
    RPAREN = r'\)'

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')
        return t

    def error(self, t):
        print(f"Illegal character: '%s'" % t.value[0] + ' at line ' + str(self.lineno))
        self.index += 1

    # comment = //

    @_(r'//.*')
    def COMMENT(self, t):
        pass

    # comment = /* */

    @_(r'/\*(.|\n)*?\*/')
    def ignore_comment_block(self, t):
        pass




class CharrParser(Parser):
    tokens = CharrLexer.tokens

    precedence = (
        ('left', PLUS, MINUS),
        ('left', TIMES, DIVIDE),
        ('right', UMINUS),
    )

    def __init__(self):
        self.lineno = None
        self.names = {}

    @_('NAME ASSIGN expr')
    def statement(self, p):
        self.names[p.NAME] = p.expr

    @_('expr')
    def statement(self, p):
        print(p.expr)

    @_('expr PLUS expr')
    def expr(self, p):
        return p.expr0 + p.expr1

    @_('expr MINUS expr')
    def expr(self, p):
        return p.expr0 - p.expr1

    @_('expr TIMES expr')
    def expr(self, p):
        return p.expr0 * p.expr1

    @_('expr DIVIDE expr')
    def expr(self, p):
        return p.expr0 / p.expr1

    @_('MINUS expr %prec UMINUS')
    def expr(self, p):
        return -p.expr

    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return p.expr

    @_('NUMBER')
    def expr(self, p):
        return int(p.NUMBER)

    @_('NAME')
    def expr(self, p):
        try:
            return self.names[p.NAME]
        except LookupError:
            print(f"Undefined name {p.NAME!r} at line {self.lineno}")
            return 0


if __name__ == '__main__':
    lexer = CharrLexer()
    parser = CharrParser()
    print(Fore.MAGENTA+
          """
       _                          _                      
      | |                        | |                     
  ___ | |__    __ _  _ __  _ __  | |  __ _  _ __    __ _ 
 / __|| '_ \  / _` || '__|| '__| | | / _` || '_ \  / _` |
| (__ | | | || (_| || |   | |    | || (_| || | | || (_| |
 \___||_| |_| \__,_||_|   |_|    |_| \__,_||_| |_| \__, |
                                                    __/ |
                                                   |___/ 

\n""", Style.RESET_ALL,
          """Charr (Lang) v0.0.1 - A language for programming. \n""")
    env = {}
    while True:
        try:
            text = input('charr: ')
        except EOFError:
            break
        if text:
            if text == 'exit':
                break
            elif text:
                parser.parse(lexer.tokenize(text))
