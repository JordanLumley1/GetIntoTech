a = 2
b = 10

# if statement
if a == b:
    print('a is equal to b')

#  if statement on a list item
lang = ['perl', 'python', 'PHP', 'Ruby']
if 'python' in lang:
    print('python is found')


# else if
if a == b:
    print('a is equal to b')
elif a > b:
    print('a is greater than b')
else:
    print('some other unexpected condition')

print('')

# chained conditionals
number = 5
distance = 43
if 0 < number < 42 < distance:
    print('num and dist are within range')
else:
    print('num and dist are out of range')

print('')

# logical AND operator on chained conditionals
if 0 < number and number < 42 and 42 < distance:
    print('num and distance are within range3')

print('')

# checks if there is any items in the list
myList = [1, 2, 3, 5, 7, 9]
if myList:
    print('The list is not empty')

print('')

# checks if a 0 is in the list and returns message
myList2 = [1, 2, 3]
if not all(myList2):
    print('not all are true')

print('')

# object types
num = 42
txt = '3'
if int(txt) < num:
    print('txt is less than num')

print('')

# while
line = None
while line != 'done':
    line = input('type "done" to complete')
    print('<', line, '>')

print('')

# while with a break, break stops loop
i = 1
while i < 8:
    print(i)
    if i == 4:
        print('The value is 4')
        break
    i+=1

print('')

# while with continue
i = 1
while i < 8:
    i+=1
    if i == 4:
        continue
    print(i)

print('')

# while with else
i=1
while i < 8:
    i+=1
    print(i)
else:
    print('i is no longer less than 8')

print('')

# for loops
fruits = ['apple', 'banana', 'orange', 'grape']
for x in fruits:
    print(x)
    if x == 'orange':
        break

print('')

# pause
drinks = ['coke', 'beer', 'squash', 'cider', 'water']
for x in drinks:
    print(x)
    if x.startswith('s'):
        break

print('')

for x in 'squash':
    print(x)

print('')
# for range
some_list = ['john', 'jack', 'joe']
for i in range(0,len(some_list)):
    print(some_list[i], i)


print('')
# for range with break
some_list = ['john', 'jack', 'joe']
for i in range(0,len(some_list)):
    print(some_list[i], i)
    if i ==2:
        break
    print(some_list[i], i)

print('')

# for range with step
# (start number, up to number, increment)
for x in range(2, 20, 3):
    print(x)
else:
    print('finished')

print('')

start = 2
end = 20
step = 3

for x in range(start, end, step):
    print(x)
else:
    print('finished')



