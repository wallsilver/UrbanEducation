"""Класс Car должен обладать следующими свойствами:
Атрибут объекта model - название автомобиля (строка).
Атрибут объекта __vin - vin номер автомобиля (целое число). Уровень доступа private.
Метод __is_valid_vin(vin_number) - принимает vin_number и проверяет его на корректность. Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
Атрибут __numbers - номера автомобиля (строка).
Метод __is_valid_numbers(numbers) - принимает numbers и проверяет его на корректность. Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
Классы исключений IncorrectVinNumber и IncorrectCarNumbers, объекты которых обладают атрибутом message - сообщение, которое будет выводиться при выбрасывании исключения."""

class Car:
    def __init__(self, model , vin, gos_number):
        self.model = model
        __vin = self.__is_valid_vin(vin)
        __numbers = self.__is_valid_numbers(gos_number)

    def __is_valid_vin(self, vin_number):
        if vin_number == True:
            raise IncorrectVinNumber(1)
        else:
            return True

    def __is_valid_numbers(self,numbers):
        if numbers == True:
            raise IncorrectCarNumbers(1)
        else:
            return True

class IncorrectVinNumber:
    def __init__ (error_):
        if error_ == 1:
            message = 'Некорректный тип vin номер'
        if error_ == 2:
            message = 'Неверный диапазон для vin номера'

class IncorrectCarNumbers:
    def __init__ (error_):
        if error_ == 1:
            message = 'Некорректный тип vin номер'
        if error_ == 2:
            message = 'Неверный диапазон для vin номера'

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')