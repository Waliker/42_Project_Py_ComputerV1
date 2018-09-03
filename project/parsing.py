import re
import sys

from utils import PolynomialParser


def equation_checker(equation):
    unauthorized_char = '[^a-zA-Z0-9\+\-\*\^\.\=]'
    if equation.count('=') != 1:
        print('SyntaxError : too many \'=\' in the equation')

    equation = re.sub('\s', '', equation)

    errors = re.findall(unauthorized_char, equation)

    if errors:
        print(errors)
        sys.exit()

    factor = set(re.findall('[a-zA-Z]', equation))
    if len(factor) != 1:
        print('The equation has to many unknown factors')
        sys.exit()

    factor = factor.pop()

    degree = re.findall(factor + '\^([0-9' + factor + ']+)', equation)
    degree = [x for x in degree if len(x) > 1 or x == factor]
    if degree:
        print('The equation degree is too high : {}'.format(degree[0]))

    return equation, factor


def equation_parser(equation):
    equation, factor = equation_checker(equation)
    left, right = equation.split(sep='=')

    left_side = PolynomialParser(left, factor)
    right_side = PolynomialParser(right, factor)

    print('Left Side : \nFactor : {} \nEquation : {}\nPolynomial list : {}'.format(
        left_side.factor, left_side.equation, left_side.degrees
    ))

    print('\nRight Side : \nFactor : {} \nEquation : {}\nPolynomial list : {}'.format(
        right_side.factor, right_side.equation, right_side.degrees
    ))
    print(left_side)
    print(right_side)

    return left_side, right_side
