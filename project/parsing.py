import re

class VariableDegree(object):
    value = 0
    exist = False
    def __init__(self, value=None, exist=None):
        if value is not None:
            self.value = value
        if exist is not None:
            self.exist = exist


class PolynomialParser(dict):

    def __init__(self, equation, x):
        dict.__init__()
        self['zero_degree'] = self.find_degree(equation, x, 0)
        self['first_degree'] = VariableDegree()
        self['seconde_degree'] = VariableDegree()

    def find_degree(equation, x, degree):
        exist = False


def equation_checker(equation):
    if equation.count('=') != 1:
        raise ValueError

    equation = equation.replace(r'\s', "")
    factor = None

    for x in equation:
        if x.isalpha():
            if factor is None:
                factor = x
            else:
                raise ValueError

    re_pattern = re.compile(factor + '\^[0-9]+')

    max_degree = re_pattern.findall(equation)

    for x in max_degree:
        if len(x) != 3 or x.find(r'[3-9]'):
            raise ValueError


def equation_parser(equation):
    parser = {}
    equation_checker(equation)
    parser['left'], parser['right'] = equation.split(sep='=')
