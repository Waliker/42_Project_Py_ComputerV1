from utils import my_sqrt


def equation_transposition(expr):
    expr = [[-x for x in item] for item in expr]

    return expr


def reduce_form(left, right):
    right = equation_transposition(right.degrees)

    left = left.reduce_form(right)
    print('The reduce form is :\n{} = 0'.format(left))
    return left


def discriminant_computation(poly):
    a = poly.degrees[2][0]
    b = poly.degrees[1][0]
    c = poly.degrees[0][0]

    discri = (b * b) - (4 * a * c)

    return second_find_solutions(discri, a, b)


def second_find_solutions(discri, a, b):
    if discri > 0:
        discri_sqrt = my_sqrt(discri, 0, 1)
        s1 = (-b + discri_sqrt) / (2 * a)
        s2 = (-b + - discri_sqrt) / (2 * a)
        print('Discriminant is striclty positive, the two solutions are :\n{}\n{}'.format(s1, s2))


def first_find_solution(poly):
    print('Polynomial degree : 1')
    solution = -poly.degrees[0][0] / poly.degrees[1][0]
    print('The solution is :\n{}'.format(solution))


def equation_solver(poly):
    if not poly.degrees[2]:
        return first_find_solution(poly)
    discri, a, b = discriminant_computation(poly)
