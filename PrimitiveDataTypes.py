# Floats
x = 4.0
y = 2.0

# Addition
print(x + y)

# Subtraction
print(x - y)

# Multiplication
print(x * y)

# Returns the quotient
print(x / y)

# Returns the remainder
print(x % y)

# Absolute value
print(abs(x))

# x to the power y
print(x ** y)

print('\n')

# Strings
x = 'Cake'
y = 'Cookie'

# Concatenate
print(x + '&' + y)

# Repeat
print(x * 2)

# Range Slicing
z1 = x[2:]

print(z1)

# Slicing
z2 = y[0] + y[1]

print(z2)

# Concatentate with Alpha-Numeric Characters
x = '4'
y = '2'

print(x + y)

# Capitalize Strings
print(str.capitalize('cookie'))

# Find the Length of a String (Spaces Included)
str1 = "Cake 4 U"
str2 = "404"

print(len(str1))

# Check if String Consists of Only Digits
print(str1.isdigit())

print(str2.isdigit())

# Replace Parts of Strings with Other Strings
print(str1.replace('4 U', str2))

# Finding Substrings 
# (Returns the Lowest Index Within the String at Which the Substring is Found)
str1 = 'cookie'
str2 = 'cook'

print(str1.find(str2))

str1 = 'I got you a cookie'
str2 = 'cook'

print(str1.find(str2))

print('\n')

# Boolean
x = 4
y = 2

print(x == y)

print(x > y)

z = (x == y) # Comparison expression (Evaluates to false)

if z: # Conditional on truth/false value of 'z'
    print("Cookie")

else: print("No Cookie")