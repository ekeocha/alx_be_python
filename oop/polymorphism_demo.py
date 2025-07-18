import math

# Base Class
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must override this method")

# Derived Class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Derived Class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Polymorphic Behavior
def print_area(shape):
    print(f"The area is: {shape.area()}")

# Example usage
if __name__ == "__main__":
    rectangle = Rectangle(10, 5)
    circle = Circle(7)

    print_area(rectangle)  # Output: The area is: 50
    print_area(circle)     # Output: The area is: 153.93804002589985
