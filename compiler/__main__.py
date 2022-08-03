import argparse
import sys
from sys import argv
from compiler.parser import CharrParser
from compiler.lexer import CharrLexer
from compiler.execute import CharrExecute


# def main():
#     if len(argv) <= 1:
#         shell()
#     else:
#         fp = argv[1]
#         execute(fp)

def main():
    lexer = CharrLexer()
    parser = CharrParser()
    env = {}
    with open('example.charr file', 'r') as f:
        for line in f:
            print("\n")
            code = parser.parse(lexer.tokenize(line))
            print('code:', code)
            CharrExecute(code, env)
            print("\n")


if __name__ == '__main__':
    main()

# -----------------


# file_open = input("Enter the CharrLang file to run: ")
# f = open(file_open, 'r')
# lexer = CharrLexer()
# parser = CharrParser()
# file_data = f.read()
#
# code = parser.parse(lexer.tokenize(file_data))
#
# create_sln = open("create_sln.charr", "w")
# create_sln.write("Solution: \n".join(str(code) for code in code))
# create_sln.close()
# open(file_open, 'r')
# data = f.readlines()
# for line in data:
#     lexer = CharrLexer()
#     parser = CharrParser()
#     result = parser.parse(lexer.tokenize(line))
