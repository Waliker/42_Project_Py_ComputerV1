#! /bin/python3

from project.parsing import equation_parser


def main():
    """Main entry point to the program.
    Retrieves the equation before parsing
    """
    equation = input('Please enter the polynomial equation to resolve : ')

    try:
        reduce_form = equation_parser(equation)
    except Exception:
        print('The current equation has not a correct format. Please correct it')
        return


if __name__ == "__main__":
    main()
