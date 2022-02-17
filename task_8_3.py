from functools import wraps


def type_logger(calc_cube):
    @wraps(calc_cube)
    def decor(*argv):
        if calc_cube > 0:
            return 'calc_cube(' + ', '.join([f'{calc_cube(x)}:{type(calc_cube(x))}' for x in argv]) + ')'
        else:
            return 'calc_cube(' + ', '.join([str(calc_cube(x)) for x in argv]) + ')'
        return decor


@type_logger
def calc_cube(x):
    return x ** 3
