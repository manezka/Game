class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def rectangle_area(self):
        return self.length * self.width

rectangle2 = Rectangle(5,7)
print(rectangle2.rectangle_area())
