
#
# define a function.
def first_function():
    print('my very first python function')
# call the function.
first_function()

# passing arguments to functions.
def second_function(first_name):
    print('my name is ' + first_name)

second_function('Jordan')
second_function('Robert')
second_function('Lumley')

def third_function(first_name, last_name):
    print('my full name is ' + first_name + " " + last_name)

third_function('jordan', 'lumley')
# error will occur because both arguments haven't been supplied.
# third_function('jordan')

def fourth_function(*params):
    print('The number of arguments is ' + str(len(params)) + ' and the first item in our argument list is ' + params[0])
fourth_function('test')
fourth_function('test', 'test2')

def fith_function(first_name, last_name):
    print('My full name is ' + first_name + " " + last_name)
fith_function(first_name='Jordan', last_name='Lumley')

# Multiple arguments with unspecified parameter names.
def sixth_function(**params):
    print('The first argument is ' + params['name'])
sixth_function(name='Jordan')

def seventh_function(**params):
    print('The first argument is ' + params['fname'] + ' and the second is ' + params['lname'])
seventh_function(fname='Jordan', lname='Lumley')

def eighth_function(age=30):
    print('My age is ' + str(age))
eighth_function(31)
eighth_function()

# Functions accepting a list as an argument.
list_of_countries = ['uk', 'canada', 'spain']
def countries_function(countries):
    print('The number of countries is ' + str(len(countries)) + ', and their names are: ')
    for x in countries:
        print(x)

countries_function(list_of_countries)

# Functions using return key word.

def number(num):
   return num
print(number(5))
same_number = number(5)
print(same_number)

# Using pass keyword to ignore function to be added to later.
def same_function():
    pass

def factorial(num):
    if num == 1:
        return 1
    else:
        return(num * factorial(num-1))

number = 6
print('The factorial of ' + str(number) + ' is ' + str(factorial(6)))

print('')
print('')

result =3
def scope_test1():
    result = 42

scope_test1()
print(result)

def scope_test2():
    global result
    result = 42

scope_test2()
print(result)

def scope_test3():
    global result
    result = 4127

scope_test3()
print(result)

