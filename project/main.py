#! /bin/python3

from parsing import equation_parser
from solver import reduce_form, equation_solver


def main():
    """Main entry point to the program.
    Retrieves the equation before parsing
    """
    equation = input('Please enter the polynomial equation to resolve : ')

    left, right = equation_parser(equation)

    left = reduce_form(left, right)

    equation_solver(left)


if __name__ == "__main__":
    main()
