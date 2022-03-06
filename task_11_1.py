from datetime import date


class Date:
    def __init__(self, date):
        self.date = date.split('-')

    @classmethod
    def typing(cls, date):
        try:
            day, month, year = [int(i) for i in date.split('-')]
            return f'{type(day), day}\n{type(month), month}\n' \
                   f'{type(year), year}'
        except ValueError:
            return 'Wrong date!'

    @staticmethod
    def validation(date):
        try:
            day, month, year = date.split('-')
            date(int(day), int(month), int(year))
            return 'Right date!'
        except ValueError:
            return 'Wrong date!'


print(Date.typing('13-06-1956'))
print(Date.validation('19-09'))
