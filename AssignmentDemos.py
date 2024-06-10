# Sequence unpacking = Allows you to take object in a collection and store them in variables for later use
x, y, z = 1, 2, 3
print(x, y, z)

# Switching values
x = 1 
y = 2
x, y = y, x
print(x, y)

# Works with variables that are sequences too
# Values below = tuples (Collection of objects seperated by commas. Similar to a list in terms of indexing, 
# nested objects, and repitition, BUT a tuple is immutable (cannot be changed/modified))
values = 1,2,3
print(values)

x,y,z = values

print(x,y,z)

# Works with dictionaries too 
scoundrel = {'first_name': 'Robin', 'last_name': 'Hood'}

# This is a good way of pulling out of a dictionary
key, value = scoundrel.popitem()
print(f'key: {key} value: {value}')

key, value = scoundrel.popitem()
print(f'key: {key} value: {value}')

# Not enough values! This gives a value error
# x,y,z = 1,2

# Too many values! This also gives a value error
#x,y,z = 1, 2, 3, 4

# using * variable
# * treats this as a list
# Filled in available values, then made a list with remaining, stored into rest(can be any variable name that you want)
x,y,*rest = 1,2,3,4,5,6,7
print(x,y,rest)

# Putting value in middle
# Takes everything remaining in the middle and adds into a list
first,*middle,last = 1,2,3,4,5,6,7
print(first,middle,last)

# With names
name = input('Please enter your full name: ')
elements_of_name = name.split()
print(elements_of_name)
first,*middle,last = elements_of_name
print(first,middle,last)