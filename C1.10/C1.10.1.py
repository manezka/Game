class Rectangle:
    def __init__(self, x, y, wight, height):
        self.x = x
        self.y = y
        self.wight = wight
        self.height = height

    def get_parameters(self):
        return print("Rectangle (" + str(self.x) + ',' + str(self.y) + ',' + str(self.wight) + ',' + str(self.height) + ")")

rect_1 = Rectangle(5, 10, 50, 100)
rect_1.get_parameters()