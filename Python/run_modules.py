

from account import account
from person import person
from dog import dog
from dog import bulldog
from shape import square
from shape import circle



some_account = account(100)
some_account.deposit(500)
some_account.deposit(100)
some_account.withdraw(200)
print(some_account.getbalance())

jay = person("jay", 20)
jay.getinformation()

# Base / super class
maindog = dog("justin")
print(maindog.bark())

# derived class
bdog = bulldog("justin ", "bulldog")
print(bdog.run())


square = square("name", 5, 5)
print(square.area())

circle = circle("name", 10, 3.14)
print(circle.circarea())

