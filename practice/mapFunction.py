nums = [48,6,2,1]

sqauare = map(lambda num: num*num,nums)
print(list(sqauare))

def area (num):
    return num * num

print(list(map(area,nums)))

print(list(filter(lambda x:x < 100,map(area,nums))))

countries_asia = ["Bhutan", "", "","China","Myanmar","", "India", "Indonesia","", "Philippines", "Singapore"]
print(list(filter(None,countries_asia)))


#Reduce
from functools import reduce
print(reduce(lambda x,y : x+y,nums))
print(reduce(lambda x,y: x * y,nums))