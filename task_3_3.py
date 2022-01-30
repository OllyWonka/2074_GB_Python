def thesaurus(*args):
    res = {}
    for i in args:
        key = i[0].capitalize()
        if key not in res:
            res[key] = []
        res[key].append(i)
    return res


print(thesaurus('Иван', 'Мария', 'Петр', 'Илья'))
