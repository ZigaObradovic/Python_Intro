
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")
        

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
    
    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius ** 2}")
        super().describe()

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, is_filled, height, width):
        super().__init__(color, is_filled)
        self.height = height
        self.width = width

circle = Circle("red", True, 5)
square = Square(color="blue", is_filled=False, width=6)

print(square.color)
circle.describe()
square.describe()