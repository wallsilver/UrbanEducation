my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
number = 0 # Индекс списка
while my_list[number] >= 0:
    if number == len(my_list) - 1: # Условия для последнего элемента списка с прерыванием
        print(my_list[number])
        break
    elif my_list[number] == 0: # Условие для нулевого значения в списке
        number = number + 1
        continue
    print(my_list[number]) # Тело цикла
    number = number + 1 # Перейти к следующему элементу в списке
