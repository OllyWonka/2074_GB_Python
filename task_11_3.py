class Err(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


if __name__ == '__main__':
    my_lst = []
    while True:
        try:
            data = input()
            if data == 'stop':
                break
            elif not data.isdigit():
                raise Err()
            else:
                my_lst.append(int(data))
        except Err:
            print('it is not a number!')

    print(*my_lst)
