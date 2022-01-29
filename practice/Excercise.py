#1
#Write a function that computes the area of a circle given its radius.
import math
def area(a):
    return math.pi * a * a
print(area(10))

#2
#
def calculation(x,y):
    return x+y,x-y
print(calculation(10,5))

#3
from functools import reduce
nums = [1,2,3,4,5]
print(reduce(lambda x,y : x*y,nums))
# loom for

#4