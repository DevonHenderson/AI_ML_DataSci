# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 13:14:29 2024

@author: Devon Henderson

Python Practical A
Week 1 - Lecture 1
"""
########################################################################
### Basic Print Statement
print("\nBASIC VARIABLES, PRINT, AND TYPES")
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

#Getting user input #REMOVED TO SPEED UP CONSOLE RETURN
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

########################################################################
### Using Mathematical functions
## Direct copy from lecture notes
import math
print("\nMATHEMATICAL FUNCTIONS")
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

########################################################################
### Random Number Functions
import random
import time
print("\nRANDOM AND TIME IMPORT FUNCTIONS")
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

########################################################################
### Working with Strings
print("\nWORKING WITH STRINGS")
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

########################################################################
### Built-in string methods
print("\nBUILT-IN STRING METHODS")
name2 = "bobby"
print("Capitilise the string: ", name2.capitalize())
print("Lower to Uppercase: ", name2 + " ", name2.upper())
print("Count char/*args in string (b): ", name2.count("b"))
print("Find args if occurs and return index (o = True): ", name2.find("o"))
print("Find args if occurs and return index (x = False): ", name2.find("x"))
print("Get length of the string: ", len(name2))
print("Split string at char/*args: ", name2.split("o"))

########################################################################
### Working with Lists
# Items belonging to a list can be of different data types
print("\nWORKING WITH LIST DATA")
multi_list = ["abc", 123, 3.14, 'HELLO', 40.4040]
small_list = [60, "Brian"]
print("Complete list: ", multi_list)
print("First element of list: ", multi_list[0])
print("Last element of list: ", multi_list[-1])
print("List elements 1->3: ", multi_list[1:3])
print("List from 3rd element: ", multi_list[2:])
print("small_list duplicated (*3): ", small_list*3)
print("Concatenated Lists: ", multi_list + small_list)
multi_list[0] = "Replace" # Replace element in list[pos]
print("Show altered list: ", multi_list)

########################################################################
### Built-in List functions
print("\nBUILT-IN LIST FUNCTIONS")
list1 = [2,4,7,3,8]
print("List length | len(): ", len(list1))
print("Return highest value from list | max(): ", max(list1))
print("Return minimum value from list | min(): ", min(list1))

########################################################################
### Built-in List methods
print("\nBUILT-IN LIST METHODS")
list_methods  = ["a","e","i","o"]
print("Index of a list value: | index(\"i\"): ", list_methods.index("i"))
list_methods.append("u")
print("Append value to list | append(\"u\"): ", list_methods)
list_methods.insert(0, "a")
print("Insert list value at position | insert(0,\"a\"): ", list_methods)
list_methods.pop()
print("Remove last value in list | pop(): ", list_methods)
list_methods.remove("e")
print("Remove specified value from list: ", list_methods)
print("Count values in list | count(\"a\"): ", list_methods.count("a"))

########################################################################
### Sorting lists
print("\nSORTING LISTS")
sorting_list = [5,2,9,4,1,0,2]
print("Original List: ", sorting_list)
sorting_list.sort()
print("Sorted list | sort(): ", sorting_list)
sorting_list.reverse()
print("Reverse list sorting | reverse(): ", sorting_list)

########################################################################
### Dictionaries
print("\nDICTIONARIES")
dict_grades = {'Ben': 79, 'Mark': 84, 'Lucas': 92}
print("dict_grades data: ", dict_grades)
print("Ben's Grades from dict | dict_grades[\"Ben\"]: ", dict_grades["Ben"])
dict_grades["Lucas"] = 94
print("Update dict entry | dict_grades[\"Lucas\"]=94: ", dict_grades["Lucas"])
print("Show all dict keys | dict_grades.keys(): ", dict_grades.keys())
print("Show all dict values | dict_grades.values(): ", dict_grades.values())
del dict_grades["Mark"]
print("Entry removed from dict | del dict_grades[\"Mark\"] : ", dict_grades)
print("Return number of items in dict | len(dict_grades): ", len(dict_grades))
if "Bob" in dict_grades: # Get True/False on dict items
    print("Found!")
for key in dict_grades:
    print(key + ": " + str(dict_grades[key]))

########################################################################
### Using basic operators in python
print("\nPYTHON BASIC OPERATORS")
print("Addition |  3+16: ", 3+16)
print("Subtraction | 50-42: ", 50-42)
print("Multiplication | 5*7: ", 5*7)
print("Division | 6/2: ", 6/2)
print("Modulo | 15%4: ", 15%4)
print("Exponentials | 2**8: ", 2**8)

########################################################################
### Using Relational operators to compare values
print("\nPYTHON COMPARISON OPERATORS")
print("Equal to bool | 2==2: ", 2==2)
print("Equal to bool | 2==3: ", 2==3)
print("Not Equal to bool | 2!=2: ", 2!=2)
print("Not Equal to bool | 2!=3: ", 2!=3)
print("Less than comparison | 2<2: ", 2<2)
print("Less than comparison | 2<3: ", 2<3)
print("Inclusive less than comparison | 2<=2: ", 2<=2)

########################################################################
### Various assignment operators on int values
print("\nASSIGNMENT OPERATORS")
x = 1
print("Original 'x' value: ", x)
x += 1
print("Incremented 'x' value | x+=1: ", x)
x *= 3
print("Mulitplies increment onto 'x' variable| x*=3: ", x)
x /= 2
print("Division increment onto 'x' variable | x/=2: ", x)
x %= 2
print("Modulo increment onto 'x' variable | x%=2: ", x)

########################################################################
### Working with logic (True, False, And, Or, Not)
print("\nLOGICAL OPERATORS")
print("True and True: ", True and True)
print("True and False: ", True and False)
print("True or False: ", True or False)
print("not True: ", not True)

########################################################################
### Identity operators
print("\nIDENTITY OPERATORS")
x = 100
y = 25*4
print("x(100) is y(25*4): ", x is y)

########################################################################
### Checking if items are 'in' lists 
print("\nMEMBERSHIP OPERATORS")
print("3 in [1,2,4,5]: ", 3 in [1,2,4,5])
print("3 in [3,6,7,8]: ", 3 in [3,6,7,8])

########################################################################
### Conditional Statements
print("\nCONDITIONAL STATEMENTS")
positive_num = 2
print("positive_num: ", positive_num)
if positive_num <= 5:
    print("Value of positive_num is less than or equal to 5")
elif positive_num <= 10:
    print("Value of positive_num variable is larger than 5 but less or equal than 10")
else:
    print("Value of positive_num is larger than 10")

########################################################################
### Loops - While Loop
print("\nWHILE LOOP")
count = 0
while (count < 5):
    print("The current count is: ", count)
    count += 1
print("End of count check")

########################################################################
### Loops - For Loop
print("\nFOR LOOP")
for letter in "Alphabet":
    print("Current Letter: ", letter)

print("USING FOR LOOP TO SHOW ALL VALUES IN LIST")    
fruits = ["Apple", "Mango", "Grape", "Blackcurrant"]
for fruit in fruits:
    print('Current fruit: ', fruit)
    
print("RANGE OF NUMBERS USING FOR LOOP + STEP VALUES")    
for i in range(1,100,15):
    print("The value of i is: ", i)

## Using break to control loop execution termination
print("USING BREAK IN A FOR LOOP")    
for letter in "Devon":
    if letter == "o":
        break
    print("Current Letter: ", letter)
    
## Using continue to return to beginning of the loop
print("USING CONTINUE IN A FOR LOOP")    
for letter in "Devon":
    if letter == "o":
        continue
    print("Current Letter: ", letter)
    
## Using pass to give null execution
print("USING PASS IN A FOR LOOP")    
for letter in "Devon":
    if letter == "o":
        pass # Code could be added in the future
    print("Current Letter: ", letter)
    
########################################################################
### Functions
print("\nFUNCTIONS")
def printStringUpper(string):
    print("String original: ", string, "\nConverted to upper: ", string.upper())    
printStringUpper("testing the uppercase")


# Pass variable and change within function
print("SHOW VALUES MODIFIED DURING RUNTIME OF FUNCTION")
def appendToList(numbers_list):
    numbers_list.append(1000)
    print("Values of list inside function: ", numbers_list)
    return
numbers_list = [1,10,100]
print("numbers_list initial values: ", numbers_list)
appendToList(numbers_list)
print("Values outside function after called: ", numbers_list)

# Reordering argument names during function calls
# caller identifies arguments by parameter name, parameter order does not matter
def printInformation(name, age=35):
    print("Name:", name)
    print("Age: ", age)
    return
print("TESTING ARGS OUT OF ORDER | age, name ")
printInformation(age = 27, name = "Devon")
print("TESTING DEFAULT ARGS VALUES IN FUNCTION | (age = 35)")
printInformation(name="Devon")

# Returning values
def sumTwoNumbers(num1, num2):
    return num1 + num2
print("To total of 15 + 27.2 is | sumTwoNumbers(15, 27.2): ", sumTwoNumbers(15, 27.2))

# Anonymous Functions
print("\nUSING ANONYMOUS FUNCTIONS")
sum = lambda arg1, arg2: arg1 + arg2
print("sum = lambda arg1, arg2: arg1 + arg2 | sum(30,20): ", sum(30,20))

########################################################################
## Scope of Variables
print("\nSCOPE OF VARIABLES")
total = 0
def sum(num1, num2):
    total = num1 + num2
    print("Total value inside function (local): ", total)
    return total

returned_total = sum(10,15)
print("Total value outside function (global): ", total)
print("Value returned by function: ", returned_total)

########################################################################
#END OF FILE
########################################################################