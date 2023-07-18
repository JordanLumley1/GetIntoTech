# a variable is a place to store data that can change
# python is a dynamically-typed language a.k.a weakly-typed
# javascript is a strongly-typed language a.k.a statically-typed

# python variable - we just give it a name

first_name = 'Jordan'
print(first_name)
print(type(first_name))

last_name = "Lumley"
print(last_name)
print(type(last_name))


# -----------------------------------------------------------------------
# This is not python this is javascript

# string firstName = "Jordan";

# -----------------------------------------------------------------------

# Learning how to do concatenation (gluing strings together)

print(first_name)
print(last_name)

full_name = first_name + last_name

print(full_name)

full_name_with_space = first_name + ' ' + last_name

print(full_name_with_space)


# this is called operator overloading
chips = 2.50
fish = 4.50
total_cost = chips + fish

print(total_cost)
# '+' is either a concatenation when given strings to work with
# or '+' is addition when given numbers to work with


dinner = 2.50
dinner = dinner + fish
# dinner = dinner + mushy_peas

print('The price of dinner is £' + str(dinner))
# long hand version of this syntax

# this is the shorthand syntax
dinner += fish
print('The price of dinner is £' + str(dinner))
