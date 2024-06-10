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