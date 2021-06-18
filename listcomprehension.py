
l = [letter for letter in 'This is character list']
print(l)


evenList = [i*2 for i in range(10)]
print(evenList)

numns = [13,12,45,42]

even_nums = [number for number in numns if number % 2 ==0]
print("Even Numbers",even_nums)

sq = [num ** 2 for num in range(11)]
print("Squares:'",sq)

sqsq = [sq*2 for sq in [num ** 2 for num in range(11)]]
print("Doubel sq:",sqsq)
print()