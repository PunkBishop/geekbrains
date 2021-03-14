value = int(input('Введите положительное число: '))

days = value // 86400
hours = (value % 86400) // 3600
minutes = (value % 3600) // 60
seconds = value % 60

if days > 0:
    print(days, ' дн ', hours, ' час ', minutes, ' мин ', seconds, ' сек')
elif hours > 0:
    print(hours, ' час ', minutes, ' мин ', seconds, ' сек')
elif minutes > 0:
    print(minutes, ' мин ', seconds, ' сек')
else:
    print(seconds, ' сек')