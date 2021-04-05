import sys


def add_sale():
    with open('bakery.csv', 'a', encoding='utf-8') as base:
        if len(user_input[1:]) == 1:
            base.write(f'{user_input[1]}\n')
        elif len(user_input[1:]) > 1:  # Можно передавать 1 запросом сразу несколько значений
            for i in user_input[1:]:
                base.write(f'{i}\n')


user_input = sys.argv
add_sale()
