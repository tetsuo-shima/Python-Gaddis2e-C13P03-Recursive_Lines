__author__ = 'dwight'

# Write a recursive function that accepts an integer argument, n . The function should display n lines of asterisks on
# the screen, with the first line showing 1 asterisk, the second line showing 2 asterisks, up to the n th line which
# shows n asterisks.

import random


def main():
    lines = random.randint(1, 15)
    print('Number of Lines:', lines)
    print_lines_recursive(lines)


def print_lines_recursive(n):
    if n > 0:
        print_lines_recursive(n - 1)
        print_asterisks(n)


def print_asterisks(number):
    for x in range(0, number):
        print('*', end='')
    print()


main()