def transform_string(number: int) -> str:
    if n % 10 == 1 and n % 100 != 11:
        return f'{n} процент'
    elif 1 < n % 10 < 5 and not 11 < n % 100 < 15:
        return f'{n} процента'
    else:
        return f'{n} процентов'


for n in range(1, 101):
    print(transform_string(n))
