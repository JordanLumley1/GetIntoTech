# Basic string - single and multiline
somestring = "Sky"

somestring1 = """
First line
Multiline string
last line
"""
print(somestring1)

# String Character Sequence Position
print(somestring[0])
print(somestring[1])

# String length
print(len(somestring))

# Loop over string
for x in somestring:
    print(x)

# Some String method
number = 3
Astring = '3'
# Converts to int - int(string)
print(number + int(Astring))

# String to upper / lower
print(somestring.upper())
print(somestring.lower())

full_name = "Lewis Oliver Clarke"
print(full_name.upper())
print(full_name.lower())
print(full_name.title())
print("The length of this is", len(full_name), "characters")

# String Replace - does not fully replace it makes a temp. copy
names = "John, Doe"
print(names.replace('John', 'Jane'))
print(names)

# Search a string
print(names.find('Doe'))
print('Doe' in names)

# Slicing - substring
john = (names[0:4])
print(john)

# Slice from start to a position can leave blank ie [:4]
print(names[:4])
# Slice from any position to end can leave blank ie [5:]
print(names[5:])

# Strip or remove whitespace from a string using strip, rstrip or lstrip

names2 = "    John, Doe    "
print(names2.strip())
print(names2.lstrip())
print(names2.rstrip())

# Concatenate strings
first = "Lewis"
last = "Clarke"
my_full_name = first + " " + last
print(my_full_name)

age = 33
message = "I am "+str(age)+" years old"
print(message)

# Format
message1 = "I am {} years old and I like {}"
print(message1.format(age, "Pythons"))

# Endswith Startswith are case-sensitive
message3 = "Welcome to python"
print(message3.startswith("Welcome"))
print(message3.endswith("python"))

# Split a string in to a list
message4 = "Welcome to python's coolness"
print(message4.split())
split_list = message4.split()
for x in split_list:
    print(x)
print(split_list[2])

# escape characters
print('')
print('')

message5= "Hello world, it is \"sunny\" today"
print(message5)

message6= "hello world, it is \n sunny today"
print(message6)
