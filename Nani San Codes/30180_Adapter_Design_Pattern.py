class Rectangle:
    def __init__(self, width : int, height : int):
        self.width = width
        self.height = height

class Square:
    def __init__(self, side_length : int):
        self.side_length = side_length
        
class Calculator:
    def calculate_area(self, rectangle : Rectangle):
        area = rectangle.width * rectangle.height
        return area

class CalculatorAdapter:
    def get_area(self, square : Square):
        calculator = Calculator()
        rectangle = Rectangle(8, 6)
        rectangle.width = rectangle.height = square.side_length
        return calculator.calculate_area(rectangle)

# Test

square = Square(5)
adapter = CalculatorAdapter()
area = adapter.get_area(square)
print(f"Area of the square: {area} square units")