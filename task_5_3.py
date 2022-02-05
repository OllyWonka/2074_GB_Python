tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
classes = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def check_gen(tutors: list, classes: list):
    for i in range(len(tutors)):
        yield tutors[i], classes[i] if i < len(classes) else None
        pass


generator = check_gen(tutors, classes)
print(type(generator))
for _ in range(len(tutors)):
    print(next(generator))
next(generator)
