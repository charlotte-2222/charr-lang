import argparse


from compiler.parser import CharrParser
from compiler.lexer import CharrLexer


if __name__ == '__main__':
    argparse=argparse.ArgumentParser(description='A simple language for programming in Charr Lang')
    argparse.add_argument('filename', metavar='filename', type=str, help='runn a Charr file')
    args=argparse.parse_args()

    f=open(args.filename, 'r')
    code=f.read()
    f.close()
    if not code:
        print('No code to run')
        exit(1)
    lexer=CharrLexer()
    parser=CharrParser()
    tokens=lexer.tokenize(code)
    program=parser.parse(tokens)
    if not program:
        exit(1)
    scope=parser.names
    program.exec(scope)