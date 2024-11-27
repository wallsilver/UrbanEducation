def test_function():
    item = ''
    def inner_function():
        nonlocal item
        item = "Я в области видимости функции test_function"
        return item
    print(inner_function())
    return item

print(test_function())


