class Mammel:
    def eat(self):
        print('eat')


class Dog(Mammel):
    def bark(self):
        print('Bark')


class Cat(Mammel):
    def be_annoying(self):
        print('annoying')

cat1 = Cat()
cat1.be_annoying()
cat1.eat()

deg1 = Dog()
deg1.eat()
deg1.bark()