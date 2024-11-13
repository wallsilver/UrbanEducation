# Функция проверяющая входение:
def single_root_words(root_word, *other_words):
    def_result = list()
    for i in other_words:
        if root_word.lower() in str(i).lower():
            def_result.append(i)
        elif str(i).lower() in root_word.lower():
            def_result.append(i)
    return def_result

# Начальные данные:
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
