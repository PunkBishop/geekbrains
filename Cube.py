numbers_array = [i ** 3 for i in range(1001) if i % 2 != 0]
sum_numbers = 0
print(f"Массив элементов = {numbers_array}")

for i in range(500):
    if numbers_array[i] % 7 == 0:
        sum_numbers += numbers_array[i]
print(f"Сумма всех чисел которые деляться на 7 = {sum_numbers}")
sum_numbers = 0

for i in range(500):
    numbers_array[i] += 17
    if numbers_array[i] % 7 == 0:
        sum_numbers += numbers_array[i]
print(f"Новый массив элементы которого увеличены на 17 = {numbers_array}")

print(f"Сумма всех чисел массива элементы которого увеличенны на 17 и деляться на 7 = {sum_numbers}")
