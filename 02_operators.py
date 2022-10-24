#print(True)
#print(False)

#Arithmetic Operators in Python
#Integers

print('Addition: ', 1 + 2)
print('Subtraction: ', 2 - 1)
print('Multiplication: ', 2 * 3)
print('Division: ', 4 / 2) # Divisions in Python gives floating number (2.0)
print('Division without the remainder: ', 7 // 2)
print('Division without the remainder: ', 7 // 3) # Gives without the floating number
print('Modulus: ', 3 % 2)
print('Exponentiation: ', 2 ** 3)

#Example: Floats
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)

#Complex numbers
print ('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ', (1 + 1j) * (1 - 1j))

#Declaring the variable at the top first

a = 3
b = 2

#Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

print(total)
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

# Connecting the dots and start making use of what i alredy know

#Calculate area of circle
radius = 10
area_of_circle = 3.14 * radius ** 2
print("Area of a circle: ", area_of_circle)

#Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print("Area of a rectangle: ", area_of_rectangle)

#Calculating a weight od an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')

#Density of a liquid
mass = 75
volume = 0.075
density = mass / volume
print(density)

"""
Conparison Operators
"""

print(3 > 2)
print(3 >= 2)
print(3 < 2)
print(2 < 3)
print(2 <= 3)
print(3 == 2)
print(3 != 2)
print('True == True', True == True)
print('True == False', True == False)
print('False == False', False == False)

"""
In addition to the above comparison operator Python uses:

*is: Returns true if both variables are the same object(x is y)
*is not: Returns true if both variables are not the same object(x is not y)
*in: Returns True if the queried list contains a certain item(x in y)
*not in: Returns True if the queried list doesn't have a certain item(x in y)
"""

print(1 is 1)
print(2 is not 1)
print(4 is 2 ** 2)

#Logical Operators

#and
print("And: ", 3 > 2 and 4 > 3)
hello_one = "hello"
hello_two = "hello"
print("And: ", hello_one and hello_two)
print("And ", True and False)
print("And ", True and True)
print("And ", 3.14 and 3.14)

#or
print("Or: ", 5 > 1 or 6 < 3)
print("Or: ", 5 > 1 or 6 > 3)
print("Or: ", 12 < 11 or 14 < 13)

#not
print("Not: ",not 3 > 2) #  # False - because 3 > 2 is true, then not True gives False
print("Not: ",not 3 < 2)
print(not True)
print(not False)
print('---------')
print(not not True)
print(not not not False)
