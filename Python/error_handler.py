def divide(a, b):
    try:
        if b == 0:
            raise ValueError("Error occured: Division by zero")
        result = a/b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: One of the values has the wrong data type.")
    except Exception as e:
        print("An unexpected error occured with details: " + str(e))
        return None
    else:
        print("No errors are raised")
    finally:
        print("Finally block run")
    try:
        result = divide(first_num, second_num)
        print("Result is" + result)
    except ValueError as v:
        print(v)



first_num = 5
second_num = 0

result = divide(5, 0)
print("result is :" + str(result))

result = divide(first_num, second_num)
print("Result is: " + str(result))

result = divide(10, 2)
print("result is :" + str(result))

