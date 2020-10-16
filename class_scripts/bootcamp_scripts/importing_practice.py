# function
def func():
	print()

#library is a collection of function
def func():
	print()

def func2():
	print()

# os library 
import os

# import library and set alias
import numpy as np

# from library import function
# from numpy import arange

from custom_functions import *

# using an os function
os.system('ls -l')

# using np 
num_list = [5,7,9,12,200]
# calculate the mean
list_average = np.mean(num_list)
print(list_average)
# generate numbers list
more_nums = np.arange(50)
print(more_nums)

# running our custom functions
say_hello('Rob')

converted_temp = fahrenheit_to_celcius(70)
print(converted_temp)

# using all of our imported library functions
# make an array of integers between 70 and 80
temps_f = np.arange(70, 81)
print(temps_f)

# loop over each temp and convert it to celcius
for f in temps_f:
	c = fahrenheit_to_celcius(f)
	print(f'{f} fahrenheit is {c} celsius')
s {c} celsius')