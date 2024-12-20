"""
Каждый объект класса UrTube должен обладать следующими атрибутами и методами:

 Атриубты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users с такими же
логином и паролем. Если такой пользователь существует, то current_user меняется на найденного. Помните, что password
передаётся в виде строки, а сравнивается по хэшу.
Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список, если
пользователя не существует (с таким же nickname). Если существует, выводит на экран: "Пользователь {nickname} уже
существует". После регистрации, вход выполняется автоматически.
Метод log_out для сброса текущего пользователя на None.
Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если с таким же
названием видео ещё не существует. В противном случае ничего не происходит.
Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово.
Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела), то ничего
не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр. После текущее время
просмотра данного видео сбрасывается.

Для метода watch_video так же учитывайте следующие особенности:

Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае выводить в консоль
надпись: "Войдите в аккаунт, чтобы смотреть видео"
Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+. Должно
выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
После воспроизведения нужно выводить: "Конец видео"
"""
#from site import USER_BASE
from time import sleep


class UrTube:

    def __init__(self):
        self.users = [] # (список объектов User)
        self.videos = [] # (список объектов Video)
        self.current_user = None # (текущий пользователь, User)
        self.current_video = None  # (текущее видео)
        self.user = None
    #def __str__(self, print_search):


    def add (self,  *args):
        i = 0
        while True:
          if args[i].title not in self.videos:
                self.videos.append(args[i].title)
                if len(args)-1 == i:
                    break
                else:
                    i+=1
    def get_videos(self, search_title):
        search_video = []
        for i in self.videos:
            if search_title.lower() in i.lower():
                search_video.append(i)
        return search_video


    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f'Пользователь {nickname} уже существует')
        else:
            self.users.append(nickname)
            self.user = User(nickname, hash(password),age)
            self.current_user = nickname
            # self.current_user = nickname


    def watch_video(self,cinema):
        self.current_video = Video.find(Video,cinema)
        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        elif cinema in self.videos:
            if self.current_video.adult_mode == True and self.user.age < 18:
                print('Вам нет 18 лет, пожалуйста покиньте страницу')
            if self.current_video.adult_mode == False or \
            (self.current_video.adult_mode == True and self.user.age > 18):
                for i in range(self.current_video.duration):
                    self.current_video.time_now += 1
                    print (self.current_video.time_now,end=' ')
                    sleep(1)
                print('Конец видео')
                self.current_video.time_now = 0

"""
Каждый объект класса Video должен обладать следующими атрибутами и методами:

Атриубуты: title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)), 
adult_mode(ограничение по возрасту, bool (False по умолчанию))
"""
class Video:
    VideoBase = []
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self. adult_mode = adult_mode
        self.__class__.VideoBase.append(self)

    def find(self, cinema):
        for i in range(len(self.VideoBase)):
            if cinema == Video.VideoBase[i].title:
                return Video.VideoBase[i]

"""
Каждый объект класса User должен обладать следующими атрибутами и методами:

Атриубуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
"""
class User:
    UserBase = []
    def __init__(self,nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
        self.__class__.UserBase.append(self)
        #print(self.age)

    def find(self, nickname):
        for nickname in User.UserBase:
            if nickname in User.UserBase:
                return self.age


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
# Добавление видео
ur.add(v1, v2)
# Проверка поиска

print(ur.get_videos('лучший'))

print(ur.get_videos('ПРОГ'))



# Проверка на вход пользователя и возрастное ограничение

ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'lolkekcheburek', 13)

ur.watch_video('Для чего девушкам парень программист?')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)

ur.watch_video('Для чего девушкам парень программист?')



# Проверка входа в другой аккаунт

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

print(ur.current_user)



# Попытка воспроизведения несуществующего видео

ur.watch_video('Лучший язык программирования 2024 года!')