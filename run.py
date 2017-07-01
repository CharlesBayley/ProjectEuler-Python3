#!/usr/bin/python3
# Problem Runner
# --------------
# Overseer Program
# ================
# This program will be in charge of calling the problems python files.
#

from importlib import import_module
from sys import argv

def load_problem(num):
    name = 'problems.p{}.main'
    numname = str(num)
    while len(numname) < 3:
        numname = '0' + numname
    return import_module(name.format(numname))


def main(args):
    problemn = 0
    try:
        problemn = args[1]
    except IndexError:
        print('The first argument should be the number of the problem you '
                + 'wish to run!')
    problem = load_problem(problemn)
    print(problem.main(None))

if __name__ == '__main__':
    main(argv)
