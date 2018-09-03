import re


class PolynomialParser:

    def __init__(self, equation, x):
        self.factor = x
        self.equation = self.split_equation(equation, x)
        self.degrees = self.find_degrees(self.equation)
        self.eval_all_degrees()

    def split_equation(self, equation, x):
        new_eq = re.split('([+-]?)\*' + x + '(\^[0-2])([+-]?)', equation)
        new_eq = [x for x in new_eq if x != '']
        print('new eq : ', new_eq)
        return new_eq

    def find_degrees(self, equation):
        value = 1.0
        sign = 1
        degrees = list(([], [], []))

        for x in equation:
            if '-' in x:
                sign = -1
            elif '+' in x:
                pass
            elif '^' in x:
                degrees[int(x[1])].append(sign * value)
                sign = 1
                value = 1
            else:
                value = float(x)

        return degrees

    def eval_degree(self, degree):
        if len(self.degrees[degree]) > 1:
            new_value = self.degrees[degree][0]
            for value in self.degrees[degree][1:]:
                new_value = new_value + value
            self.degrees[degree] = [new_value]

    def eval_all_degrees(self):
        it = 0
        for degree in self.degrees:
            self.eval_degree(it)
            it += 1

    def reduce_form(self, other_polynome):
        self.degrees = [x + y for (x, y) in list(zip(self.degrees, other_polynome))]
        self.eval_all_degrees()
        return self

    def __repr__(self):
        ret = ""
        it = 0

        for degree in self.degrees:
            if degree:
                if ret:
                    ret = ret + ' + ' + str(degree[0]) if degree[0] > 0 else ret + ' ' + str(degree[0])
                    ret = ret + ' * ' + self.factor + '^' + str(it)
                else:
                    ret = str(degree[0]) + ' * ' + self.factor + '^' + str(it)
            it += 1

        ret = ret.replace('-', '- ')
        return ret


def my_sqrt(number, x, a):
    while x * x < number:
        x += a
    if x * x == number:
        return x
    else:
        return my_sqrt(number, x - a, a / 10)
