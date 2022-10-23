# Day2: 30 Days of python programming

first_name = 'Santiago'
print(first_name, ": ", type(first_name), "length: ", len(first_name))

last_name = 'Guex'
print(last_name, ": ", type(last_name), "length: ", len(last_name))

full_name = first_name + " " + last_name
print(full_name, ": ", type(full_name))

country = 'Argentina'
print(country, ": ", type(country))

city = 'La Rioja - Chilecito'
print(city, ": ", type(city))

age = 15
print(age, ": ", type(age))

year = 2.022
print(year, ": ", type(year))

is_married = False
print(is_married, ": ", type(is_married))

is_true = True
print(is_true, ": ", type(is_true))

is_light_on = True
print(is_light_on, ": ", type(is_light_on))

dad, mom, sister = "Nicolas", "Maria", "Candela"
print(dad, ": ", type(dad))
print(mom, ": ", type(mom))
print(sister, ": ", type(sister))

print('--------------------')

"""
Values

num_one = 5

num_two = 4

diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two / num_one
floor_division = float(num_one) / float(num_two)
"""

"""
radius of a circle is 30 meters
"""

radius_of_circle = int(input("Value for radius: "))
diameter = radius_of_circle*2
pi = 3.14

area_of_circle = pi * radius_of_circle*radius_of_circle

circum_of_circle = diameter * pi

print("Area of circle: ", area_of_circle)
print("Circumference of circle: ", circum_of_circle)

"""
Use the built-in input function to get first name, last name, country and age from a user and store 
the value to their corresponding variable names.
"""

f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")
f_country = input("Enter your country: ")
f_age = input("Enter your age: ")
print(f_name, l_name, f_country, f_age)