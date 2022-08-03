from compiler.lexer import CharrLexer
from compiler.parser import CharrParser
from compiler.execute import evaluate, VERSION

if __name__ == "__main__":
    lexer = CharrLexer()
    parser = CharrParser()
    while True:
        try:
            print("------------------------------------------------------\n"
                  f"Charr Lang {VERSION} Shell\n")
            text = input('-> ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            evaluate(tree)
