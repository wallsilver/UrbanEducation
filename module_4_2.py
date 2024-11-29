def test_function(): # п. 1
#    item = ''
    def inner_function(): # п. 2
        print ('Я в области видимости функции test_function') # п. 2
        #    return item
    inner_function() # п. 3
#    return item

#print(inner_function()) # п. 4 error - NameError: name 'inner_function' is not defined

test_function() # Не входит в задание, но даёт смысл п.3
inner_function() # п. 4
