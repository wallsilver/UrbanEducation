my_string = input("Введите любые символы: ")
print("Количество символов в ведённом Вами тексте pавно: " , int(len(my_string)))
print("Ваш текст в верхнем pегистpе: " , my_string.upper())
print("Ваш текст в нижнем pегистpе:" , my_string.lower())
print("Ваш текст без пробелов: " , my_string.replace(" ", ""))
print("Ваш текст начинается с символа: '" + my_string[0] + "'")
print("Ваш текст заканчивается символом: '" + my_string[-1] + "'")

