class shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass
    def perimeter(self):
        pass

class square(shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width
        self.name = "square"

    def area(self):
        return (self.length * self.width)

class circle(shape):
    def __init__(self, name, diam, pi):
        super().__init__(name)
        self.diam = diam
        self.pi = pi
        self.name = "circle"
    def circarea(self):
        return (self.diam * self.pi)










