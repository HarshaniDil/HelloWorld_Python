import random

for i in range(1):
    print(random.randint(1, 10))  #This is  use in integer

members = ['Ishan', 'Harshani', 'vindi', 'Thilosha']

leader = random.choice(members) # Choice from list of string
print(leader)


class Dice:
    def roll(self):
        for i in range(1):
            first = random.randint(1,6)
            second = random.randint(1,6)
        return first,second


dice1 = Dice()
print(dice1.roll())