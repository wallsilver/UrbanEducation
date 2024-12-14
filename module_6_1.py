class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        _cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        pass

    def get_cords(self):
        print(f'X, {_cords[0]}, Y {_cords[1]}, Z {_cords[2]}')

    def attack(self):
        _DEGREE_OF_DANGER = super()._DEGREE_OF_DANGER
        if super()._DEGREE_OF_DANGER > 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0" )

    def speak(self):
        print(f'{self.sound}')

class Bird(Animal):
    beak = True

    def lay_eggs(self):
        print (f'Here are(is) {round(1,4)} eggs for you')

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        pass

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    sound = "Click-click-click"
#    _DEGREE_OF_DANGER = super.__init__(_DEGREE_OF_DANGER)

db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
#db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()

