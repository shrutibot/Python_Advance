class Shape:
    def __init__(self, color):
        self.color = color

    def describe(self):
        print(f"I am a shape, and my color is {self.color}.")


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color) #inherit color from paremt class
        self.radius = radius

    def calculate_area(self):
        return 3.14*self.radius**2
    
    def describe(self):
        super().describe() #Call paremt class describe method
        print(f"I am also a cicle with radius{self.radius}.")

circle1=Circle("red",5)
circle1.describe()
circle1.calculate_area() #Acsess specific child method
