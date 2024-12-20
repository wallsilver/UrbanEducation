def calculate_structure_sum(*args):
    sum_all=0
    for i in args:
        if isinstance(i, str):
            sum_all += len(i)
        elif not isinstance(i, int):
            sum_all += _type(i)
        else:
           sum_all += i
    return sum_all

# Обработчик типов
def _type (type_):
    sum_type=0
    for i in type_:
        if isinstance(i, tuple):
            sum_type += _tuple(i)
        elif isinstance(i, list):
            sum_type += _list(i)
        elif isinstance(i, dict):
            sum_type += _dict(i)
        elif isinstance(i, str):
            sum_type += len(i)
        else:
            sum_type += i
    return sum_type

# Обработчик картежей
def _tuple(*tuple_):
    sum_tuple = 0
    for j in tuple_:
        if not isinstance(j, int):
            sum_tuple += _type(j)
        else:
            sum_tuple += j
    return sum_tuple

# Обработчик списков
def _list(list_):
    list_sum=0
    for i in list_:
        if not isinstance(i, int):
            list_sum += _type(i)
        else:
            list_sum += i
    return list_sum

# ОБработчик словарей
def _dict(dict_):
    sum_dict=0
    for key in dict_:
        sum_dict +=len(key)
        sum_dict += int(dict_[key])
    return sum_dict


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)