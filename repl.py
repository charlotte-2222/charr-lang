from compiler.lexer import CharrLexer
from compiler.parser import CharrParser
from compiler.execute import VERSION, CharrExecute

if __name__ == "__main__":
    lexer = CharrLexer()
    parser = CharrParser()
    env = {}
    print("------------------------------------------------------\n"
          f"Charr Lang {VERSION} Shell\n")
    while True:
        try:
            text = input('-> ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            CharrExecute(tree, env)


