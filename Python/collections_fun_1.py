person1 = 'Melissa'
person2 = 'Rob'
person3 = 'Serene'
person4 = 'callum'

# This is a tuple, a tuple doesn't need to contain the word tuple.
# they are defined by the commas.
person_tuple = 'Melissa', 'Rob', 'Serene', 'Callum'
print(type(person_tuple))
print(person_tuple)

# This tuple has brackets, it will print with or without brackets.
second_tuple = ('Jordan', 'Lewis')
print(type(second_tuple))
print(second_tuple)

# This prints Rob from person_tuple (0,1,2,3).
print(person_tuple[1])

# Both of the below print callum.
# 0 and Positive numbers read from left to right.
print(person_tuple[3])
# Minus numbers read from right to left.
print(person_tuple[-1])

# Tuples can also contain booleans.
marmite_lover = True, True, False
print(marmite_lover)
# TUPLES ARE IM-MUTABLE can not change.
# Tuples can also contain numbers.

# Commas for tuple [] square brackets for list.
# LISTS ARE MUTABLE can change.
lucky_numbers = [5, 8, 13]
print(lucky_numbers)
print(type(lucky_numbers))

# Square brackets make lists, items separated by commas.
names_list = ['stephen', 'Mark', 'Nav', 'Nik', 'Lewis']
print(names_list)
print(type(names_list))

# Method for adding to list.
names_list.append('Melissa')
print(names_list)

# Dictionaries.
# Key value pairs.
# Adds one piece of data to another.
numbers_dictionary = {'Mark': 5, 'Lewis': 8, 'Rob': 2}
print(numbers_dictionary)
print(type(numbers_dictionary))

# Sets.
# A unique collection.
# Does not allow duplicates and removes them, info can be in a different order.
names_set = {'Lewis', 'Nick', 'Serene', 'Nav', 'Lewis', 'Stephen'}
print(names_set)
print(type(names_set))

