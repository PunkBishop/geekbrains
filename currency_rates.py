import requests


def currency_rates(charcode):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    r = requests.get(url)
    date_0 = r.text.split('Date="')
    date = (date_0[1].split('" name="'))
    for content_rates in r.text.split('<CharCode>')[1:]:
        content_0 = content_rates.split('</Value>')[0].split('</CharCode><Nominal>')
        currency_code = content_0[0]
        content_1 = content_0[1].split('</Nominal><Name>')
        currency_nom = content_1[0]
        content_2 = content_1[1].split('</Name>')
        currency_name = content_2[0]
        content_3 = content_2[1].split('<Value>')
        currency_value = content_3[1].replace(',', '.')
        if currency_code == charcode:
            print(f"{currency_nom} рубль(ей) = {round(float(currency_value), 2)} {currency_name}, "
                  f"данные актуальны на {date[0]}")
            break
        if currency_code == 'JPY' and currency_code != charcode:
            print(None)


code = str(input('Введите код валюты:\n'))
currency_rates(code.upper())

currency_rates('USD')
currency_rates('EUR')
