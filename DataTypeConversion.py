# Check the Type of an Object
i = 4.0

print(type(i))

# Implicit Data Type Conversion (Coercion)

# A Float
x = 4.0

# An Integer
y = 2

# Divide 'x' by 'y'
z = x/y

# Check the type of 'z'
print(type(z))

# Explicit Data Type Conversion
x = 2
y = "The Godfather: Part "

# fav_movie = y + x # Results in a TypeError

fav_movie = (y) + str(x)

print(fav_movie)