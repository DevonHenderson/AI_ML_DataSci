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

print("\nBUILT-IN CLASS ATTRIBUTES")
print(emp1.__dict__) #Dict containing the classes namespace
print(emp1.__doc__)  #Class documentation string (none if undefined)
print(emp1.__class__.__name__) #Class name
print(emp1.__module__) #Module(library) name in which the class is defined


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
        
class Child(Parent): #define child to inherit from Parent class
    def __init__(self):
        super().__init__() #Call the parent class constructor
        print("Calling child constructor")
        
    def childMethod(self):
        print("Calling child method")
        
c=Child()
print("--------------")
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()
########################################################################
#END OF FILE
########################################################################