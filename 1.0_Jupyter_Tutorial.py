# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 12:21:42 2024

@author: Devon Henderson

Introduction to Jupyter Notebooks
Week 1 - Lecture 1
"""
########################################################################
### Simple print statement
print("\nSIMPLE PRINT STATEMENT")
a = 10
print("A has the value of: ", a)

########################################################################
#### Managing the IPython Kernel
print("\nUSING IMPORT TIME")
import time
#time.sleep(10) #Commented to remove wait time

########################################################################
### Crash Python to restart kernel
# DO NOT UNCOMMENT THIS
# import os
#os._exit(0)

########################################################################
### stdout and stderr
print("\nUSING STDOUT/STDERR")
import sys
print("stdout")
print("stderr", file=sys.stderr)

### Errors
b = '120'
#if b.endswith(0):
    #print(b) # Error expected due to incorrect datatype

########################################################################    
### Asynchronous output check
print("\nSHOWING ASYNCHRONOUS OUTPUT")
for i in range(8):
    print(i)
    time.sleep(0.1)

########################################################################    
### Large outputs
print("\nSHOW LARGE OUTPUTS")
for i in range(20):
    print(i) #console will jump to bottom of print statements (no wait)

########################################################################    
### Checking object details
import collections
#collections.namedtuple? #Commented to shorten console output time

### Get source code of a given object
#collections.Counter??  #Commented to shorten console output time

### Computation Outputs
# The output of a computation is stored in the variable _
2+10
#_+10 #only works in notebooks

### Check history of executed code
#%history -n 1-5

########################################################################
### Magic functions (% and --)
print("\nUSING 'MAGIC' FUNCTIONS")
#%magic
#%timeit list(range(1000))
for i in range(1,5):
    size = i*10
    print('size:', size, end=" ")
    #%timeit list(range(size))
    
########################################################################
### Plotting with MatPlotLib
print("\n\nUSING MATPLYLIB.PYPLOT AND NUMPY")
print("see Plots tab")
import matplotlib.pyplot as plot
import numpy as np
x = np.linspace(0,3*np.pi, 500)
plot.plot(x, np.sin(x**2))
plot.title('A simple chirp')

########################################################################
### Basic Display Imports
from IPython.display import (
    display_pretty,
    display_html,
    display_jpeg,
    display_png,
    display_json,
    display_latex,
    display_svg
)
from IPython.display import Image
i = Image(filename='images/ipython_logo.png')
display(i)
