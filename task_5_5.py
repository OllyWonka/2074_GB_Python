def get_uniq_numbers(src: list):
    for num in range(len(src)):
        if src.count(num) == 1:
            yield src[num]
            pass


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))
