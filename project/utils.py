import re


class PolynomialParser:

    def __init__(self, equation, x):
        self.factor = x
        self.equation = self.split_equation(equation, x)
        self.degrees = self.find_degrees(self.equation)
        self.eval_all_degrees()

    def split_equation(self, equation, x):
        pattern_degree = '([-+]?\\d+(?:\\.\\d+)?)?\\*?(' + x + ')?\\^?(\\d+)?'
        polynomes = re.findall(pattern_degree, equation)
        return polynomes

    def find_degrees(self, polynomes):
        deg = {}

        for x, y, z in polynomes:
            if any(map(len, (x, y, z))):
                k = z if z is not None else '1' if y is not None else '0'
                if k in deg:
                    deg[k].append(float(x)) if x else deg[k].append(float(1))
                else:
                    deg[k] = [float(x)] if x else [float(1)]

        return deg

    def eval_max_degree(self):
        m_degree = '0'
        for key in self.degrees.keys():
            if m_degree < key:
                m_degree = key
        self.max_degree = m_degree

    def eval_degree(self, degree):
        if len(self.degrees[degree]) > 1:
            new_value = self.degrees[degree][0]
            for value in self.degrees[degree][1:]:
                new_value = new_value + value
            self.degrees[degree] = [new_value]

    def eval_all_degrees(self):
        for degree in self.degrees.keys():
            self.eval_degree(degree)

        self.degrees = {k: v for k, v in sorted(self.degrees.items()) if v and v[0] != 0}
        self.eval_max_degree()

    def reduce_form(self, other_polynome):
        new_dict = {}
        merge_dict = sorted(self.degrees.items()) + sorted(other_polynome.items())
        for k, v in merge_dict:
            if k in new_dict:
                new_dict[k] += v
            else:
                new_dict[k] = v
        self.degrees = new_dict
        self.eval_all_degrees()
        return self

    def __repr__(self):
        ret = ''
        for k, v in self.degrees.items():
            if ret and v[0] >= 0:
                ret = ret + '+ '
            ret = ret + str(v[0]) + ' * ' + self.factor if k > '0' else ret + str(v[0])
            ret = ret + '^' + k + ' ' if k > '1' else ret + ' '

        ret = ret.replace('-', '- ')
        if not ret:
            ret = '0 '
        return ret


def my_sqrt(number, x, a):
    while x * x < number:
        x += a
    if x * x == number:
        return x
    else:
        return my_sqrt(number, x - a, a / 10)
