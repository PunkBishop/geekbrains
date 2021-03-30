def generator_tuple(list_1, list_2):
    for tutor, klass in zip(list_1, list_2):
            yield tutor, klass


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

scool = generator_tuple(tutors, klasses)

print(next(scool))
print(next(scool))
print(next(scool))
print(next(scool))
print(next(scool))
print(next(scool))
print(next(scool))
print(next(scool))
