class dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("woof")

    def run(self):
        print(self.name + "is running")

class bulldog(dog):
    def __init__(self, name, breed):
        super().__init__(name)
        # self.breed = "bulldog"
        self.breed = breed

    def bark(self):
        print("wooooo")

    def stroke(self):
        print("stroking" + self.name)

