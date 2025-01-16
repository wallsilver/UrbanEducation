"""Задача "Банковские операции":
Необходимо создать класс Bank со следующими свойствами:

Атрибуты объекта:
balance - баланс банка (int)
lock - объект класса Lock для блокировки потоков.

Метод deposit:

Будет совершать 100 транзакций пополнения средств.
Пополнение - это увеличение баланса на случайное целое число от 50 до 500.
Если баланс больше или равен 500 и замок lock заблокирован - lock.locked(), то разблокировать его методом release.
После увеличения баланса должна выводится строка "Пополнение: <случайное число>. Баланс: <текущий баланс>".
Также после всех операций поставьте ожидание в 0.001 секунды, тем самым имитируя скорость выполнения пополнения.
Метод take:

Будет совершать 100 транзакций снятия.
Снятие - это уменьшение баланса на случайное целое число от 50 до 500.
В начале должно выводится сообщение "Запрос на <случайное число>".
Далее производится проверка: если случайное число меньше или равно текущему балансу, то произвести снятие, уменьшив
balance на соответствующее число и вывести на экран "Снятие: <случайное число>. Баланс: <текущий баланс>".
Если случайное число оказалось больше баланса, то вывести строку "Запрос отклонён, недостаточно средств" и
заблокировать поток методом acquiere.
Далее создайте объект класса Bank и создайте 2 потока для его методов deposit и take. Запустите эти потоки.

После конца работы потоков выведите строку: "Итоговый баланс: <баланс объекта Bank>"."""


import threading
from threading import Lock
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            deposit =  randint(50, 500)
            self.balance += deposit
            print(f'Пополнение: {deposit}. Баланс: {self.balance}')
            #Event.wait(self,1)
            if self.balance >= 500 and self.lock.locked() == True:
                self.lock.release()
            sleep(0.001)
    def take(self):
        for i in range(100):
            take = randint(50, 500)
            print(f'Запрос на {take}')
            if take <= self.balance:
                self.balance -= take
                print(f'Снятие: {take}. Баланс: {self.balance}')
            if take > self.balance:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bk = Bank()
event = threading.Event()
# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')