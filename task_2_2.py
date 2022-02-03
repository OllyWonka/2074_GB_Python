def convert_list_in_str(list_in: list) -> str:
    list_another = []
    for i in list_in:
        if i.isdigit():
            i = int(i)
            list_another.append(f'"{i:02d}"')
        elif i[0] == '+':
            i = int(i[1:])
            list_another.append(f'"{i:02d}"')
        elif i[0] == '-':
            i = int(i[1:])
            list_another.append(f'"{i:02d}"')
        else:
            list_another.append(i)
    str_out = ' '.join(list_another)
    return str_out


my_list = ['в', '5', 'часов', '17', 'минут', 'температура',
           'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)
