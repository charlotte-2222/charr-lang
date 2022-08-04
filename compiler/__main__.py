from compiler.shell import *
from compiler.parser import CharrParser
from compiler.lexer import CharrLexer
from compiler.execute import CharrExecute

import os


def main():
    lexer = CharrLexer()
    parser = CharrParser()
    env = {}

    print("Welcome to the Charr Language Compiler\n"
          "Option | Description | Command \n"
          "-------|-------------|------- \n"
          "Shell | Run the Charr Shell | Enter 'shell'\n"
          "Compile | Compile a Charr File (.charr), default option. | Enter absolute file pathing to a .charr file\n"
          "Exit | Exit the compiler | Enter 'exit' \n"
          "------------------------------------------------------\n")

    while True:
        file = input("-> ")
        if file == "shell":
            while True:
                shell()
        elif file == "exit":
            exit(1)
        else:
            with open(file, 'r') as f:
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
