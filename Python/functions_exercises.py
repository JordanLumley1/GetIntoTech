def area_function(len, width):
    return len * width

print (area_function(4, 2))


print('')
print('')

def even_odd_function(num):
    if (num % 2) ==0:
        print('The number entered: ' + str(num) + '. This number is even.')
    else:
        print('The number entered: ' + str(num) + '. This number is odd.')
even_odd_function(4)

print('')
print('')

def word_frequency(sentence):
    counts = {}
    words = sentence.split()

    for word in words:
        word = word.strip(',')
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

print(word_frequency("My name is, jordan and i'm learning how to write functions"))

