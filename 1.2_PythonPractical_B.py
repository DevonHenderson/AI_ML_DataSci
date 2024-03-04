# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 16:52:49 2024

@author: Devon Henderson

Python Practical B
Week 1 - Lecture 1
"""
########################################################################
### Python Classes/Objects
print("\nCLASSES AND OBJECTS")
class Employee:
    'Common base class for all employees' #Documentation String
    emp_Count = 0
    
    def __init__(self, name, salary): #Class Constructor 
        self.name = name 
        self.salary = salary
        Employee.emp_Count += 1
        
    def displayCount(self): #Method of the class
        print("Total Employee %d" % Employee.emp_Count)
        
    def displayEmployee(self):
        print("Name: ", self.name, ", Salary: ", self.salary)

# Creating Instance objects
emp1 = Employee("Eren", 5000)
emp2 = Employee("Armin", 3500)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total number of Employee class instantiated: %d" % Employee.emp_Count)

emp1.age = 16 #Adds a new attribute
print(emp1.name, emp1.age)
del(emp1.age)
print(hasattr(emp1, "age")) #Should return false as "age" deleted
print(hasattr(emp2, "name"))

########################################################################
print("\nBUILT-IN CLASS ATTRIBUTES")
print(emp1.__dict__) #Dict containing the classes namespace
print(emp1.__doc__)  #Class documentation string (none if undefined)
print(emp1.__class__.__name__) #Class name
print(emp1.__module__) #Module(library) name in which the class is defined

########################################################################
print("\nCLASS INHERITANCE")
class Parent:
    parentAttr = 100
    
    def __init__(self):
        print("Calling parent constructor")
        
    def parentMethod(self):        
        print("Calling parent method")
        
    def setAttr(self, attr):
        Parent.parentAttr = attr
        
    def getAttr(self):
        print("Parent attribute: ", Parent.parentAttr)
    
    def overrideTest(self):
        print('Calling parent method')
        
class Child(Parent): #define child to inherit from Parent class
    def __init__(self):
        super().__init__() #Call the parent class constructor
        print("Calling child constructor")
        
    def childMethod(self):
        print("Calling child method")
        
    def overrideTest(self): # override parent method
        print('Calling child method')
        
c=Child()
print("---")
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()
print("---")
c = Child()          # instance of child
c.overrideTest()         # child calls overridden method
## Both parent and child have overrideTest but only child.overrideTest will call

########################################################################
### Vector Overloading Example
print("\nVECTOR OVERLOAD PARAMS")
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self): #Overloading print method
        return('Vector (%d, %d)' % (self.x, self.y))
    
    def __add__(self, other):  #Overloading addition method
        return Vector(self.x + other.x, self.y + other.y)

a = Vector(4, 2)
b = Vector(1, 5)
c = a + b # plus operator has been overloaded by the vector class implementation
print(c)  # the vector class also overloaded the print method


########################################################################
### Data Hiding 
print("\nPUBLIC / PRIVATE ATTRIBUTES SCOPE")
class JustCounter:
    __secretCount = 0 #__ hides attribute outside class
    publicAttr = "This is a public attribute"
    
    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)
        
counter = JustCounter()
counter.count()
counter.count()
print(counter.publicAttr)
# print(counter.__secretCount) #Error for trying to access private attr


########################################################################
### Using other files as modules with import
print("\nIMPORTING FUNCTIONS FROM FILES")
import support #In same filepath called support.py
support.print_func("Devon")
support.squared_Func(10)

from support import squared_Func # Can import functions from modules
squared_Func(5) #Removes need for module prefix to function

from support import * #imports all functions from module (take care with duplicate func names)
print_func("Testing the import * code")

########################################################################
### Namespaces and Scoping
Money = 2000

def AddMoney():
    global Money
    Money += 1
    
print(Money)
AddMoney()
print(Money)

greeting = "Hello"
def SayHi(name):
    text = "Hello, " + name + "!"
    print(locals())
SayHi("Devon")
# print(globals())
print(dir(support))



########################################################################
#END OF FILE
########################################################################