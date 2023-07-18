def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: One of the values has the wrong data type.")
    else:
        print("No errors are raised")

first_number = input("Please type in your first number: ")
second_number = input("Please type in your second number :")

first_number = int(first_number)
second_number = int(second_number)

print(first_number)
print(second_number)

result = divide(first_number, second_number)
print("result is :" + str(result))