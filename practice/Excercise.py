
#1
#Write a function that computes the area of a circle given its radius.
import math
def area(a):
    return math.pi * a * a
print(area(10))

#2  Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of it.
# And also it must return both addition and subtraction in a single return call
def calculation(x,y):
    return x+y,x-y
print(calculation(10,5))

#3 Write a recursive function that prints the product of all values from an array of integer numbers,
# without using for or while loops. Can you make it tail-recursive? (Hint use Sum Example as inspiration)
from functools import reduce
nums = [1,2,3,4,5]
print(reduce(lambda x,y : x*y,nums))
# look for tail recursive

#4 Write a function that takes a milliseconds value and returns a string describing the value in days, hours, minutes, and seconds.
# What’s the optimal type for the input value?



#5 Create a function showSalary() in such a way that it should accept employee name,
# and it’s salary and display both, and if the salary is missing in function call it should show it as 5000
salfunction= lambda name,sal : print("Name :",name, " has salary: ",sal) if sal > 0 else print("Name :",name, " has salary: ",500)
salfunction("vinit",100)
salfunction("vinit",200)
salfunction("vinit",0)


#6Write a function that calculates the difference between a pair of 2D points (x and y) and returns the result as a point.
# (Hint: this would be a good use for tuples - Search Tuples Examples for inspiration).
#Reduce
from functools import reduce
inputs = ((2,3),(4,5),(8,9),(3,8))
calculateDistance = lambda xy : xy[1]-xy[0]
result = map(calculateDistance,list(inputs))
print(list(result))
addfunction = lambda x,y : x[0]+y[0]
#reducedata = reduce( addfunction,result)
#print(reducedata)

#7 Write a function that takes a 3-sized tuple and returns a 6-sized tuple, with each original parameter followed by its String representation.
# For example, invoking the function with (true, 22.25, "yes") should return (true, "true", 22.5, "22.5", "yes", "yes").
# Can you ensure that tuples of all possible types are compatible with your function? When you invoke this function,
# can you do so with explicit types not only in the function result but in the value that you use to store the result?

def convert(tuppleExample):
    newTupple = list()
    for i in tuppleExample:
         newTupple.append(i)
         newTupple.append(str(i))
    return tuple(newTupple)

tupleEx = (True,22.25,"yes")
print(tupleEx)
print(convert(tupleEx))

#8 Write a sort function for a list of 4-tuples. Below is a list of the nearest stars and some of their properties.
# The list elements are 4-tuples containing the name of the star, the distance from the sun in light years, the apparent brightness, and the luminosity.
# The apparent brightness is how bright the stars look in our sky compared to the brightness of Sirius A.
# The luminosity, or the true brightness, is how bright the stars would look if all were at the same distance compared to the Sun

startList = list ();

star1 = ("Alpha Centauri A", 4.3, 0.26, 1.56)
star2 = ("Alpha Centauri B", 4.3, 0.077, 0.45)
star3 = ("Alpha Centauri C", 4.2, 0.00001, 0.00006)
star4 = ("Barnard’s Star", 6.0, 0.00004, 0.0005)
star5 = ("Wolf 359", 7.7, 0.000001, 0.00002)
star6 = ("BD +36 degrees 2147", 8.2, 0.0003, 0.006)
star7 = ("Luyten 726-8 A", 8.4, 0.000003, 0.00006)
star8 = ("Luyten 726-8 B", 8.4, 0.000002, 0.00004)
star9 = ("Sirius A", 8.6, 1.00, 23.6)
star10 = ("Sirius B", 8.6, 0.001, 0.003)
star11 = ("Ross 154", 9.4, 0.00002, 0.0005)
startList.append(star1)
startList.append(star2)
startList.append(star3)
startList.append(star4)
startList.append(star5)
startList.append(star6)
startList.append(star7)
startList.append(star8)
startList.append(star9)
startList.append(star10)
startList.append(star11)
print(startList)

total = len(startList)
startList.sort(key = lambda x:x[1])
print(startList)
startList.sort(key = lambda x:x[2])
print(startList)
startList.sort(key = lambda x:x[3])
print(startList)