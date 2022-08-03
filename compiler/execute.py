from .lexer import CharrLexer
from .parser import CharrParser
import colorama as c
from colorama import init, Fore, Back, Style

VERSION = "0.0.1"

names = {}


class CharrExecute:

    def __init__(self, tree, env):
        self.env = env
        self.walkTree(tree)

    def walkTree(self, node):

        if isinstance(node, int):
            return node
        if isinstance(node, str):
            return node
        if isinstance(node, bool):
            return node

        if node is None:
            return None

        if node[0] == 'program':
            if node[1] == None:
                self.walkTree(node[2])
            else:
                self.walkTree(node[1])
                self.walkTree(node[2])

        if node[0] == 'num':
            return node[1]

        if node[0] == 'str':
            return node[1]

        if node[0] == 'bool':
            return node[1]

        if node[0] == 'if_stmt':
            result = self.walkTree(node[1])
            if result:
                return self.walkTree(node[2][1])
            return self.walkTree(node[2][2])

        if node[0] == 'show':
            print(self.walkTree(node[1]))

        if node[0] == 'condition_eq':
            return self.walkTree(node[1]) == self.walkTree(node[2])
        if node[0] == 'condition_le':
            return self.walkTree(node[1]) <= self.walkTree(node[2])
        if node[0] == 'condition_lt':
            return self.walkTree(node[1]) < self.walkTree(node[2])
        if node[0] == 'condition_ge':
            return self.walkTree(node[1]) >= self.walkTree(node[2])
        if node[0] == 'condition_gt':
            return self.walkTree(node[1]) > self.walkTree(node[2])
        if node[0] == 'condition_ne':
            return self.walkTree(node[1]) != self.walkTree(node[2])

        if node[0] == 'add':
            return self.walkTree(node[1]) + self.walkTree(node[2])
        elif node[0] == 'sub':
            return self.walkTree(node[1]) - self.walkTree(node[2])
        elif node[0] == 'mul':
            return self.walkTree(node[1]) * self.walkTree(node[2])
        elif node[0] == 'div':
            return self.walkTree(node[1]) / self.walkTree(node[2])

        if node[0] == 'var_assign':
            self.env[node[1]] = self.walkTree(node[2])

        if node[0] == 'show_var':
            try:
                print(self.env[node[1]])
                return self.env[node[1]]
            except LookupError:
                print("Undefined variable '"+node[1]+"' found!")
                return 0

        if node[0] == 'for_loop':
            if node[1][0] == 'for_loop_setup':
                loop_setup = self.walkTree(node[1])

                loop_count = self.env[loop_setup[0]]
                loop_limit = loop_setup[1]

                for i in range(loop_count+1, loop_limit+1):
                    res = self.walkTree(node[2])
                    if res is not None:
                        print(res)
                    self.env[loop_setup[0]] = i
                del self.env[loop_setup[0]]

        if node[0] == 'for_loop_setup':
            return (self.walkTree(node[1]), self.walkTree(node[2]))


# def shell():
#     lexer = CharrLexer()
#     parser = CharrParser()
#     print(c.Fore.MAGENTA + "------------------------------------------------------\n"
#                            f"Charr Lang {VERSION} Shell\n")
#     while True:
#         try:
#             text = input(c.Fore.LIGHTBLUE_EX + '->: ')
#         except EOFError:
#             break
#         tree = parser.parse(lexer.tokenize(text))
#         walkTree(tree, env)
