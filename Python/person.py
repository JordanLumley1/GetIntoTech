class person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.balance = 100

    def updatename(self, newname):
        self.name = newname

    def updatebalance(self, bal):
        self.balance = bal

    def getinformation(self):
        print("name is " + self.name)
        print("age is " + str(self.age))
