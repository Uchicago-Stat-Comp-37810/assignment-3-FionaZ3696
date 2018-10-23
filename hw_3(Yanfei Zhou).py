# Name:Yanfei Zhou(UCID:12207462)
# hw3.py
import math, random
from math import *


##### Template for Homework 3, exercises 1 -  ######


# ********** Exercise 1 **********

# Define is_divisible function here
def is_divisible(m,n):
    if m%n ==0:
        return True
    else:
        return False

# Test cases for is_divisible
## Provided for you... uncomment when you're done defining your function

print (is_divisible(10, 5))  # This should return True
print (is_divisible(18, 7))  # This should return False
print (is_divisible(42, 0))  # What should this return?

# ********** Exercise 2 **********

# Define not_equal function here
def not_equal(m,n):
    if m>n or m<n:
        return True
    else: return False

# Test cases for not_equal
print (not_equal("a","a"))
print (not_equal(2,3))

# ********** Exercise 3 **********

## 1 - multadd function
def muladd(a,b,c):
    return a*b+c
## 2 - Equations
##### YOUR CODE HERE #####


# Test Cases
angle_test = sin(muladd(pi,1/4,0))+muladd(cos(muladd(pi,1/4,0)),1/2,0)
print ("sin(pi/4) + cos(pi/4)/2 is: %f" %angle_test)

ceiling_test = ceil(muladd(276,1/19,0)) + muladd(2,log(12,7),0)
print("sin(pi/4)+cos(pi/4)/2 is: %f" %ceiling_test)

# ********** Exercise 4 **********

## 1 - rand_divis_3 function
def rand_divis_3():
    a = random.randint(0,100)
    print (a)
    if a %3==0:
        return True
    else: return False

# Test Cases
rand_divis_3(18,3)
rand_divis_3(21,2)
