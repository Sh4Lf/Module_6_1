class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True  # живой
        self.fed = False   # накормлен


class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = True  # съедобный


class Mammal(Animal):
    def eat(self, food):
        if food.edible:  # еда съедобная
            self.fed = True
            print(f"{self.name} съел {food.name}")
        else:
            print(f"{self.name} не может съесть {food.name}")
            self.alive = False
            print(f"{self.name} умер")


class Predator(Animal):
    def eat(self, food):

        if isinstance(food, Plant):
            print(f"{self.name} не может съесть {food.name}")
            self.alive = False
            print(f"{self.name} умер")
        else:
            self.fed = True
            print(f"{self.name} съел {food.name}")


class Flower(Plant):
    def __init__(self, name):
       super().__init__(name)
       self.edible = False# цветы не съедобные


class Fruit(Plant):
    def __init__(self, name):
       super().__init__(name)
       self.edible = True  # фрукты съедобные


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик-семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)  # состояние жизни хищника
print(a2.fed)    # состояние сытости млекопитающего
a1.eat(p1)      # хищник пытается съесть цветок
a2.eat(p2)      # млекопитающее пытается съесть фрукт
print(a1.alive)  # снова состояние жизни хищника
print(a2.fed)    # снова состояние сытости млекопитающего

