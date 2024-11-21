def calculate_structure_sum(*args):
    sum=0
    for i in args:
        if isinstance(i, str) == True:
            sum += len(i)
        elif isinstance(i, int) != True:
            sum += _type(i)
        else:
           sum += i
    print(sum)
    return sum

def _type (type_):
    sum_type=0
    for i in type_:
        if isinstance(i, tuple) == True:
            sum_type += _tuple(i)
        elif isinstance(i, list) == True:
            sum_type += _list(i)
        elif isinstance(i, dict) == True:
            sum_type += _dict(i)
        elif isinstance(type_, str) == True:
            sum_type += len(i)
        else:
            print(type(i))

def _tuple(tuple_):
    sum_tuple = 0
    for j in tuple_:
        if isinstance(j, int) != True:
            sum_tuple += _type(j)
        else:
            sum_tuple += j
    return sum_tuple

def _list(list_):
    list_sum=0
    for i in list_:
        if isinstance(i, int) != True:
            list_sum += _type(i)
        else:
            list_sum += i
    return list_sum

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