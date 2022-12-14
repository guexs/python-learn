# Variables

my_string_variable = "Santiago"
print(my_string_variable)

my_int_variable = 15
print(my_int_variable)

#str() -> convertir otros tipos de datos a strings
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable, type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)

# Se puede pasar distintas variables o datos dentro de un mismo print (concatenacion de cadenas y variables)
print("My first name:", my_string_variable)
print(my_string_variable, str(my_int_variable), my_bool_variable)

"""
Romper los prints <class 'NoneType'>
print(type(print(my_string_variable)))
"""

# Multiple variables:
pais = "Argentina"
first_name, last_name, country, age, school = 'Santiago', 'Guex', pais, 15, 'C.P.A'

print('------------------')
print("First name: ", first_name)
print("Last name: ", last_name)
print("Country: ", country)
print("Age:", age)
print("School: ", school)
print('------------------')

"""
Getting user input using the input() built-in function
Example
"""

learning = input('What are you learnning: ')
music = input('Say a music topic: ')

print(learning) 
print(music) 