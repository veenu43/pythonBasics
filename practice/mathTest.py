import math;

def circle(radius):
    area = math.pi * radius * radius
    return area

print(circle(7) )
ciclearea = lambda radius : math.pi * radius * radius

print(ciclearea(10))


add = lambda a,b : a+b
print(add(4,3))

print((lambda x,y,z: x+y+z)(1,2,3))