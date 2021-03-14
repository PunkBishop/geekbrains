number = int(input("Введите число для склонения: "))

if number == 1:
    print(f"{number} процент")
elif number != 1 and number <= 4:
    print(f"{number} процента")
elif number > 4:
    print(f"{number} процентов")