class Point:
    def move(self):
        print('Move')

    def draw(self):
        print("draw")

point1 = Point()
point1.move()
point1.X = 10
print(point1.X)