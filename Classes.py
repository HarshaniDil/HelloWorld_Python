class Point: # First letter should be capital
    def move(self):
        print("move")

    def draw(self):
        print("draw")


Point1 = Point()
Point1.draw() # These are called objects
Point1.move()
Point1.x = 10
Point1.y = 20
print(Point1.x)
print(Point1.y)

#Let's create another object

Point2 = Point()
Point2.x=50
print(Point2.x)