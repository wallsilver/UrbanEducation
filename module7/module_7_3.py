"""
get_all_words - подготовительный метод, который возвращает словарь следующего вида:

{'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}

Где:

'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.
Алгоритм получения словаря такого вида в методе get_all_words:

Создайте пустой словарь all_words.
Переберите названия файлов и открывайте каждый из них, используя оператор with.
Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке. (тире обособлено пробелами, это не дефис
в слове).
Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.

метод, где word - искомое слово. Возвращает словарь, где ключ - название файла,
значение - количество слова word в списке слов этого файла.

метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение - позиция первого такого слова
в списке слов этого файла.
"""
class WordsFinder:

    def __init__(self, *args):
        self.file_names = []
        for i in args:
            self.file_names.append(i)

    def get_all_words(self):
        self.all_words = {}
        for i in self.file_names:
            with open(i, encoding = 'utf-8') as file:
                line_ = []
                for line in file:
                    line = line.replace(',','').replace(':','').replace('.','').\
                    replace('=','').replace('!','').replace('?','').\
                    replace(', ',' ').replace(' - ',' ').replace(':','').\
                    replace('(','').replace(')','').lower()
                    line_.extend(line.split())
            self.all_words[i] = line_

        return self.all_words

    def find(self, word):
        return_ = ''
        for i in self.file_names:
            if word.lower() in self.all_words[i]:
                return_ += (f'{i}:{self.all_words[i].index(word.lower()) + 1}\n')
        return return_

    def count(self, word):
        return_ = ''
        for i in self.file_names:
            if word.lower() in self.all_words[i]:
                return_ += (f'{i}:{self.all_words[i].count(word.lower())}\n')
        return return_
"""
В методах find и count пользуйтесь ранее написанным методом get_all_words для получения названия файла и списка его слов.
Для удобного перебора одновременно ключа(названия) и значения(списка слов) можно воспользоваться методом словаря - item().

for name, words in get_all_words().items():
  # Логика методов find или count
"""
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

# Свои проверки для нескольких файлов
finder3 = WordsFinder('test_file.txt', 'test_file1.txt', 'test_file2.txt', 'test_file3.txt')
print(finder3.get_all_words()) # Все слова
print(finder3.find('TEXT')) # 3 слово по счёту в каждом файле
print(finder3.count('teXT')) # 4 слова teXT в тексте всего в каждом файле

# Предложенная проверка
finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))