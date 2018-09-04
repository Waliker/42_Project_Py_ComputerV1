#! /bin/python3

from project.parsing import equation_parser
from project.solver import reduce_form, equation_solver


def computor(equation):
    left, right = equation_parser(equation)

    left = reduce_form(left, right)

    print('Polynomial degree : {}'.format(left.max_degree))
    solution = equation_solver(left)

    return solution


def main():
    """Main entry point to the program.
    Retrieves the equation before parsing
    """
    equation = input('Please enter the polynomial equation to resolve : ')

    computor(equation)


if __name__ == "__main__":
    main()
