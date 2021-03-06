import random
from termcolor import *


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None


    def __str__(self):
        return f'I am {self.name}, my fulness is {self.fullness}'

    def eat(self):
        if self.house.food >= 10:
            print(f'{self.name} has eaten!')
            self.fullness += 10
            self.house.food -= 10
        else:
            print(f'{self.name} has no food')

    def work(self):
        print('{} works and earns some money'.format(self.name))
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        print('{} watching MTV all the day'.format(self.name))
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            print('{} went shopping and bought food'.format(self.name))
            self.house.food += 50
            self.house.money -= 50
        else:
            print('{} money is gone!'.format(self.name))

    def go_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} accomodated in the house!!!'.format(self.name), color='green')




    def act(self):
        if self.fullness <= 0:
            print(f'{self.name} is dead.')
            return
        dice = random.randint(1,6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()




class House:

    def __init__(self):
        self.food = 10
        self.money = 50

    def __str__(self):
        return f'Food left at home {self.food}, money left at home {self.money}'


citizens = [
    Man(name='Beavis'),
    Man(name='Butthead'),
    Man(name='John')
]



my_sweet_home = House()

for citizen in citizens:
    citizen.go_house(house=my_sweet_home)

for day in range(1, 21):
    cprint('================day{}=================='.format(day), color='yellow')
    for citizen in citizens:
        citizen.act()
    print('----------------at the enf of the day-----------------------')
    for citizen in citizens:
        print(citizen)
    print(my_sweet_home)


