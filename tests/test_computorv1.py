from project.main import computor


test_inputs = [
    ('42 * X^0 = 42 * X^0', 'Infiny'),
    ('1 * X^0 + 2 * X^1 + 4 * X^2 = - 1 * X^0 + 4 * X^1 + 3 * X^2', None),
    ('1 * X^0 = 2 * X^0', None),
    ('0 * X^2 + 1 * X^2 + 1 * X^1 + 7 * X^0 = 0', None),
    '2 * X^2 - 4 * X^0 + 1 * X^1 = 3 * X^3 + 2 * X^1 - 3 * X^2 - 3 * X^3 + 3 * X^0'
]


def test_basic_inputs():
    global test_inputs

    for x, y in test_inputs:
        s = computor(x)
        assert s == y
