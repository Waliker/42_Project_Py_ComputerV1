import re
import sys

from utils import PolynomialParser


def syntax_checker(equation):
    if equation.count('=') != 1:
        print('SyntaxError : too many \'=\' in the equation')

    unauthorized_char = '[^a-zA-Z0-9\+\-\*\^\.\=]'
    errors = re.findall(unauthorized_char, equation)

    if errors:
        print(errors)
        sys.exit()

    factor = set(re.findall('[a-zA-Z]', equation))
    if len(factor) != 1:
        print('The equation has to many unknown factors')
        sys.exit()

    factor = factor.pop()

    return factor


def polynomial_checker(equation, factor):
    if re.search('[^' + factor + '0-9]$', equation) is not None:
        print('Bad syntax at the end of the string')
        sys.exit()

    polynomial_re_pattern = '^(-?(\d+(\.\d+)?)?((?:[\*+-]X|^X)(\^[0-9]+)?)?[+-]?)+$'

    match = re.match(polynomial_re_pattern, equation)
    if match is None or match.group() != equation:
        print('The equation is not well syntaxed')
        sys.exit()


def equation_checker(equation):
    equation = re.sub('\s', '', equation)

    factor = syntax_checker(equation)
    left, right = equation.split(sep='=')

    polynomial_checker(left, factor)
    polynomial_checker(right, factor)

    return left, right, factor


def equation_parser(equation):
    left, right, factor = equation_checker(equation)

    left = PolynomialParser(left, factor)
    right = PolynomialParser(right, factor)

    return left, right
