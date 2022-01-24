def sum_list_1(dataset: list) -> int:
    sum_1 = 0
    for numb in dataset:
        sum_digits = 0
        numbs = numb
        while numb != 0:
            sum_digits += numb % 10
            numb //= 10
        if sum_digits % 7 == 0:
            sum_1 += numbs
    return sum_1


def sum_list_2(dataset: list) -> int:
    sum_2 = 0
    for numb in dataset:
        numb += 17
        sum_digits = 0
        numbs = numb
        while numb != 0:
            sum_digits += numb % 10
            numb //= 10
        if sum_digits % 7 == 0:
            sum_2 += numbs
    return sum_2


my_list = list(range(1, 1000, 2))
for i in range(len(my_list)):
    my_list[i] = my_list[i] ** 3

result_1 = sum_list_1(my_list)
print(result_1)

result_2 = sum_list_2(my_list)
print(result_2)
