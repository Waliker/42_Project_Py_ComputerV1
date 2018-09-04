from utils import my_sqrt


def equation_transposition(expr):
    expr = {k: [-x for x in v] for k, v in expr.items()}

    return expr


def reduce_form(left, right):
    right = equation_transposition(right.degrees)

    left = left.reduce_form(right)
    print('The reduced form is :{}= 0'.format(left))
    return left


def discriminant_computation(poly):
    a = poly['2'][0]
    b = poly['1'][0] if '1' in poly.keys() else 0
    c = poly['0'][0] if '0' in poly.keys() else 0

    discri = (b * b) - (4 * a * c)

    return discri, a, b


def second_find_solutions(poly):
    discri, a, b = discriminant_computation(poly)
    if discri > 0:
        discri_sqrt = my_sqrt(discri, 0, 1)
        s1 = (-b + discri_sqrt) / (2 * a)
        s2 = (-b + - discri_sqrt) / (2 * a)
        print('Discriminant is striclty positive, the two solutions are :\n{}\n{}'.format(s1, s2))

    elif discri == 0:
        s = -b / (2 * a)
        print('Discriminant is equal to 0, the solution is :\n{}'.format(s))

    else:
        print('The equation has no real solution')


def first_find_solutions(poly):
    solution = -poly['0'][0] if '0' in poly.keys() else 0
    solution = solution / poly['1'][0]
    print('The solution is :\n{}'.format(solution))


def zero_find_solutions(poly):
    a = poly['0'] if '0' in poly.keys() else 0

    if a == 0:
        print('Every real numbers are solutions of this equation')
    else:
        print('The equation is false')


def equation_solver(poly):
    func_solver = [zero_find_solutions, first_find_solutions, second_find_solutions]
    if poly.max_degree > '2':
        print('The degree is too high, the equation can not be solved')
    else:
        func_solver[int(poly.max_degree)](poly.degrees)
