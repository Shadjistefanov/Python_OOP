import math

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def distance(self, x: float, y: float):
        delta_x = abs(x - self.x)
        delta_y = abs(y - self.y)
        return math.sqrt((delta_x ** 2) + delta_y ** 2)
    #return (((x * x) - x) * 2) + (((y * y) - y) * 2)

p = Point(2, 4)
p.set_x(3)
p.set_y(5)
print(p.distance(10, 2))


