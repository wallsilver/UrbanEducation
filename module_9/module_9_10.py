"""Цель задания:

Освоить механизмы создания декораторов Python.
Практически применить знания, создав функцию декоратор и обернув ею другую функцию.

Задание:
Напишите 2 функции:
Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и
"Составное" в противном случае."""
import math

def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        # список простых чисел начинается с 2, всё остальное можно сразу отмести
        if result <= 1:
            print("Составное")
            return result
        result_sqrt = int(math.sqrt(result))
        divisors = range(2, (result_sqrt + 1))
        # Если число не простое, то в отрезке от 1 до квадратного корня числа, точно будут его делители
        for element in divisors:
           if result % element == 0:
                print("Составное")
                return result
        print("Простое")
        return result
    return wrapper


@is_prime
def sum_three(a ,b, c):
    sum = a + b + c
    return sum

result = sum_three(2, 3, 6)
print(result)

result1 = sum_three(3, 3, 6)
print(result1)
