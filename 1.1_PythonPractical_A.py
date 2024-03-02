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
#username = input("Please enter a username: ")
#print("Your username is now: ", username)

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

print("\n")
### Using Mathematical functions
## Direct copy from lecture notes
import math
print("abs(-3):", abs(-3)) # The absolute value of x: the (positive) distance between x and zero.
print("math.ceil(3.3):", math.ceil(3.3)) #The ceiling of x: the smallest integer not less than x
print("math.floor(3.3):", math.floor(3.3)) #The floor of x: the largest integer not greater than x
print("round(7.3422323,2):", round(7.3422323,2)) #x rounded to n digits from the decimal point. 
print("math.exp(1):", math.exp(1))#The exponential of x: e^x
print("math.log(10):", math.log(10)) #The natural logarithm of x, for x> 0
print("math.log10(x):", math.log10(10)) #The base 10 logarithm of x, for x> 0
print("max(3,7,2):", max(3,7,2)) #The largest of its arguments
print("min(3,7,2):", min(3,7,2)) #The smallest of its arguments
print("sqrt(25):", math.sqrt(25)) # The square root of x

print("\n")
### Random Number Functions
import random
import time

"""
seed() sets integer starting value used in generating random numbers. 
Call before calling any other random module function.
"""
random.seed(time.time())
print("choice([7,2,9,3,0,1]): ", random.choice([7,2,9,3,0,1]))
print("choice('works with strings') : ", random.choice('works with strings'))

## return from a range
print("From randrange(1,20)", random.randrange(1,20))

## return random float of (0 <= 1)
print("Random Float 1: ", random.random())
print("Random Float 2: ", random.random())

## randomise list elements with shuffle()
list = [1,2,3,4,5]
print("Initial List: ", list)
random.shuffle(list)
print("Shuffled List: ", list)


print("\n")
### Working with Strings
name = "Devon"
print("Complete String: ", name)
print("First Char[0] of string: ", name[0])
print("Chars[1:3] of string: ", name[1:3])
print("String starting from char[2:]", name[2:])
print("Duplicate name: ", name*3)
print("Concatenated name: ", name + " " + "Henderson")
print("Bool from string values (a = False): ", "a" in name)
print("Bool from string values (e = True): ", "e" in name)
print("Formatted String: ", "My name is %s and I am %d years old!" % (name, 27))

print("\n")
### Built-in string methods
name2 = "bobby"
print("Capitilise the string: ", name2.capitalize())
print("Lower to Uppercase: ", name2 + " ", name2.upper())
print("Count char/*args in string (b): ", name2.count("b"))
print("Find args if occurs and return index (o = True): ", name2.find("o"))
print("Find args if occurs and return index (x = False): ", name2.find("x"))
print("Get length of the string: ", len(name2))
print("Split string at char/*args: ", name2.split("o"))

