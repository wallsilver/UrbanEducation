class User:
    """
    Класс пользавателя, содержащий аттрибуты: логин и пароль

    """
    def __init__(self, username, password1, password2 ):
        self.username = username
        if password1 == password2:
            self.password = password1

class Database:
    def __init__(self):
        self.data = {}
    def add_user(self, username, password1):
        self.data[username] = password1

if __name__ == '__main__':
    database = Database()
    while True:
        choice = input('Приветствую! Выберите действие:\n1 - Вход\n2 - Регистрация\n3 - Выход\n')
        if choice == '1':
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            if login in database.data:
                if password == database.data[login]:
                    print (f'Добро пожаловать: {login}!')
                else:
                    print( 'Проверьте вводимые данные')
            else:
                print('Пользователь не найден. Пройдите регистрацию.')
        if choice == '2':
            user = User (login := input("Введите логин: "), password := input("Введите пароль: "), password_conf := input("Ведите пароль еще раз: "))
            if password != password_conf:
                print('Пароли не совпадают, попробуйте ещё раз')
                continue
            if login in database.data:
                print('Пользователь уже существует. Выполните вход или зарегистрируйтесь с другим логином')
                continue
            database.add_user(user.username, user.password)
        if choice == '3':
            print('До свидания.')
            exit()
        print (database.data)
