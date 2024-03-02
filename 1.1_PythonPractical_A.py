# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 13:14:29 2024

@author: devon
"""

## Python Practical A
## Week 1 - Lecture 1

### Basic Print Statement
print("Hello World")

### Indentation
i = 1
if i == 1:
    print("i is equal to 1")
else:
    print("i is not equal to 1")
    
### Multiline comments
"""
This is a
comment
across multiple
lines
"""

#Getting user input
username = input("Please enter a username: ")
print("Your username is now: ", username)

# Variable Types
num_int = 1
num_float = 1.1
str_name = "Devon"
list_ints = [1, 2, 3, 4, 5]
dict_fav_foods = {"Devon":"Pizza", "Sarah":"Loaded Potato"} #Key:Value pairs in {}
num_complex = 3 + 12j

print("Int Check: ", num_int)
print("Float Check: ", num_float)
print("String Check", str_name)
print("List Check", list_ints)
print("Dict Check", dict_fav_foods)

### Converting Variables
print(int(num_float)) # Convert from Int to Float
print(float(num_int)) # Convert from Float to Int
print(complex(num_int)) #num_int from Float to Complex
print(type(num_int))