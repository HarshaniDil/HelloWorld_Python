class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self):
        print('Move')

    def draw(self):
        print("draw")


point1 = Point(10,20)
point1.y = 50
print(point1.y)


class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f"{self.name} talk")

harshani = Person('Harshani Dilrukshi')
print(harshani.name)

harshani.talk()