import random

n = random.randint(3, 20) # Генерируем случайное число для первой ячейки
list_key = list(range(1,n)) # Создаём список значений для ключа
result = [] # Создаём переменную для хранения ключа
number = 0 # Задаём начальное значение первой цифры в списке
while number < n/2-1: # Пока не достигли середины списка. Далее идут повторы пар
    for i in range(n-2):
        if n % (list_key[number] + list_key[i+1]) == 0:
            result.extend([list_key[number], list_key[i+1]])
    number = number + 1

print(f'В первом поле цифра {n}')
print('Пароль: ', *result)