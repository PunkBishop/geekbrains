class UserDivZeroError(Exception):
    def __init__(self, message):
        self.message = message


def user_div():
    while True:
        user_quit = input('Для выхода из программы напишите "Выход", если выход не требуется напишите любой символ:\n')
        if user_quit == 'Выход':
            break
        dividend = input('Введите делимое: ')
        divisor = input('Введите делитель: ')
        try:
            if float(divisor) == 0:
                raise UserDivZeroError('При делении на ноль результатом всегда будет бесконечность.')
            else:
                print(f'Частное: {float(dividend) / float(divisor):.2f}')
        except UserDivZeroError as ex:
            print(ex)
        except ValueError as ex:
            print(ex)


user_div()

if __name__ == '__main__':
    user_div()
