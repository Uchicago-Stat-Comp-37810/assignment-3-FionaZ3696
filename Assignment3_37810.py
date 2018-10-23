import math, random
from math import *

##Question 1
def is_divisible(m,n):
    if m%n ==0:
        return True
    else:
        return False

#is_divisible(18,4)
#is_divisible(21,3)

##Question2
def not_equal(m,n):
    if m>n or m<n:
        return True
    else: return False

#not_equal("a","a")
#not_equal(123,131)



##Question 3
def muladd(a,b,c):
    return a*b+c

angle_test= sin(muladd(pi,1/4,0))+muladd(cos(muladd(pi,1/4,0)),1/2,0)
print("ceiling(276/19)+2 log_7(12) is: %f" %angle_test)

ceiling_test = ceil(muladd(276,1/19,0)) + muladd(2,log(12,7),0)
print("sin(pi/4)+cos(pi/4)/2 is: %f" %ceiling_test)


##Question 4
def rand_divis_3():
    a = random.randint(0,100)
    print (a)
    if a %3==0:
        return True
    else: return False
