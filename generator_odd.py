def generator_odd(number):
    for i in range(number+1):
        if i % 2 != 0:
            yield i


number = int(input('Введите длинну множества:\n'))
number_gen = generator_odd(number)

print(f'Множество всех нечетных элементов от 1 до {number} =', end=' ')
for gen in number_gen:
    print(gen, end=' ')
