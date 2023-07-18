def user_age(age):
    try:
        if age < 0:
            raise ValueError("Error occured: positive number required.")
        result = age
        return result
    finally:
        print("")

age = int(input("Please type in your age: "))

try:
    user_age(age)
except ValueError as e:
    print("ERROR!" + str(e))

def user_name(name):
    try:
        result2 = name
        return result2
    except TypeError:
        print("Error: One of the values has the wrong data type.")

name = input("Please type in your name: ")



print("Your age is: " + str(age))
print("Your name is: " + name)

