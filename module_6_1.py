class Animal:  # Животное
    def __init__(self, name):
        self.alive = True  # (живой)
        self.fed = False  # (накормленный)
        self.name = name  # индивидуальное название каждого животного.
    def eat(self, food):
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
            if food.edible == False:
                print(f"{self.name}не стал есть {food.name}")
                self.alive = False

class Plant:  # Растение
    def __init__(self, name):
        self.edible = False  # (съедобность)
        self.name = name  # индивидуальное название каждого растения

class Mammal(Animal):  # Млекопитающее
    def __init__(self, name):
        super().__init__(name)

class Predator(Animal):  # Хищник
    def __init__(self, name):
        super().__init__(name)



class Flower(Plant):  # Цветок
    def __init__(self, name):
        super().__init__(name)


class Fruit(Plant):  # Фрукт
    def __init__(self, name):
        super().__init__(name)
        edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
