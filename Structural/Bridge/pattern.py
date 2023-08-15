

from abc import ABC, abstractmethod

class Color(ABC): # Color Base
    @abstractmethod
    def coloring():
        pass

class Red(Color):
    def coloring():
        return "Red"
    
class Blue(Color):
    def coloring():
        return "Blue"
    
class Green(Color):
    def coloring():
        return "Green"


class Shape(ABC): # Shape Base
    def __init__(self, color):
        self.color = color # Bridge

    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        return f"Dibujando un circulo de color: {self.color.coloring()}"
    
class Triangle(Shape):
    def draw(self):
        return f"Dibujando un triangulo de color: {self.color.coloring()}"
    

tst = Circle(color=Red)
print(tst.draw())