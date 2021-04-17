import re


def email_parse(email_address):
    example = re.compile(r'^(?P<username>\w+)@(?P<domain>\w+\.\w+)$')
    result = example.match(email_address)
    if not result:
        print('Вы ошиблись при написании адреса, перепроверьте написание.')
        raise ValueError('Email not correct')
    return result.groupdict()


print(email_parse('test@geekbrains.ru'))
print(email_parse('test@geekbraincom'))
