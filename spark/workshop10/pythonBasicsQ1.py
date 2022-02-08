# a) What is 8 to the power 4?

# Type 1
def powerCalc(x,y):
    powerValue =x
    while( y> 1):
        powerValue= x*powerValue
        y = y-1
    return powerValue

print(powerCalc(8,4))

# Type 2 using math
# Import math Library
import math
print(math.pow(8,4))


# b) Split this string “Split this string”
stringValue = "Split this string"
print(stringValue.split(" "))

# c) Given the variables: planet = “Earth”, diameter = 12742, use .format() to print the following string “The diameter of Earth is 12742 kilometers.”
# Type 1
planet = "Earth"
diameter = 12742
print(f"The diameter of {planet} is {diameter} kilometers.")

# type1
text1 = "The diameter of {planet} is {diameter} kilometers."
print(text1.format(planet = "Earth",diameter = 12742))

# d) Given the name list, use indexing to grab word “target”, the_list = [1,2,[3,4],[5,[100,200,['target']],23,11],1,7]
the_list = [1,2,[3,4],[5,[100,200,['target']],23,11],1,7]
#print(the_list.index(['target']))


# e) Given this nest dictionary grab the work “hello”. The_dic = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# f) Create a basic function that returns True if the word 'elephant' is contained in the input string.
# Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization.

def checkElephant(s):
    if(s.count("elephant") >0):
        return True
    else:
        return False

print("Is dog an elephant: ",checkElephant("dog"))
print("Is elephant an elephant: ",checkElephant("elephant"))
print("Is Elephant an elephant: ",checkElephant("Elephant"))

# g) Create a function that counts the number of times the word "elephant" occurs in a string. Again ignore edge cases.
def countElephant(s):
    return s.count("elephant")

print("Count: ", countElephant("jhghjelephant"))
print("Count: ", countElephant("jhghj elephant"))
print("Count: ", countElephant("jhghj Elephant"))

# h) Write a function to return one of 3 possible results: "Low speed", "Medium speed", or "Fast speed".
# If your speed is 60 or less, the result is "Low speed".
# If speed is between 61 and 80 inclusive, the result is "Medium speed".
# If speed is 81 or more, the result is "Fast speed".
# Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all cases.

def speedCheck(speed,isBirthday):
    increment = 0;
    if(isBirthday):
        increment = 5;
    result="None"
    if(speed >= 81+increment):
        result = "Fast Speed"
    elif ( 61+increment <= speed<= 80+increment):
        result = "Medium Speed"
    elif ( speed <=60+increment ):
        result = "Low Speed"
    return result

print(speedCheck(65,False))
print(speedCheck(65,True))
print(speedCheck(81,False))
print(speedCheck(81,True))