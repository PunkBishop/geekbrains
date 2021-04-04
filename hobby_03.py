import json


def add_none(first, second):
    for _ in range(len(first)):
        if len(first) > len(second):
            second.append(f'{None}')
    return second


def del_comma(list_1):
    for el in range(len(list_1)):
        list_1[el] = list_1[el].replace(',', ' ')
    return list_1


result = dict()
with open('names.txt', 'r', encoding='utf-8') as f_1, \
        open('hobby.txt', 'r', encoding='utf-8') as f_2:
    names = f_1.read().split('\n')
    hobby = f_2.read().split('\n')
    add_none(names, hobby)
    del_comma(names)
    for i in range(len(names)):
        result.setdefault(names[i], hobby[i])
with open('result.json', 'w', encoding='utf-8') as result_file:
    dict_as_string = json.dumps(result, ensure_ascii=False)
    result_file.write(dict_as_string)
