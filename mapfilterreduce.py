'''
def square(num):
    return num ** 2

input_list = range(1,11)

m1 = map(square,input_list)

print(m1)
print(list(m1))

print(list(map(lambda x: x ** 3,input_list)))


num1 = [4,5,6,1]
num2 = [5,6,7]
result = map(lambda n1,n2: n1+n2,num1,num2)
print(list(result))



alphas = ['a','b','c','d','e']
vowels = ['a','e','i','o','u']
filteredVowels = filter(lambda alpha : alpha in vowels,alphas)
print('The filtered vowels are:')
for vowel in filteredVowels:
    print(vowel)

'''
#Reduce
from functools import reduce
input_list = range(1,15)
print(reduce(lambda x,y: x+y,input_list))

#Reduce
from functools import reduce
f = lambda a,b: a if(a > b) else b
maxnum = reduce(f,[47,11,42,102,13])
print(maxnum)