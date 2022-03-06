class DivisionError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


if __name__ == '__main__':
    from sys import exit

    a = 0
    b = 0
    try:
        a = float(input('what a: '))
        b = float(input('what b: '))
    except:
        print('incorrect value!')
        exit(1)

    try:
        if b == 0:
            raise DivisionError('stop divising by Zero!')
        print(f'{a}/{b} = {a / b}')
    except DivisionError as err:
        print(err)
