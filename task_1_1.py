def convert_time(duration: int) -> str:
    d = duration // 3600 // 24
    h = duration // 3600 - d * 24
    m = duration // 60 % 60
    s = duration % 60
    return f'{d} дн {h} час {m} мин {s} сек'


duration = 400153
result = convert_time(duration)
print(result)
