'''
coordinates = [[12.0,13.3],[0.6,18.0],[88.0,1.1]]

print('first coordinate: {}'.format(coordinates[0]))
print('first coordinate: {}'.format(coordinates[0][1]))

threeDim = [[1,2,3,[10,20,30]],['A','B','C']]
print(threeDim[0][3][1])

intSeq=[0,1,2,3,4,5,6]
del intSeq[0]
print(intSeq)


languages = ['Java','C++','Go','Python','JavaScript']
if 'Python' in languages:
    print('Python is there!')

if 6 not in [1,2,3,7]:
    print('number 6 is not present')


orig=[1,2,3]
mod=orig
mod[0]=99
print('original {}, modified {}'.format(orig,mod))

name='vinit'
name1=name
name='Kumar'
print('name {},name1 {}'.format(name,name1))

'''

orig=[1,2,3]
mod=orig.copy()
mod[0]=99
orig[1]=89
print('original {}, modified {}'.format(orig,mod))


my_list=[1]
my_list.insert(4,'test')
my_list.insert(1,'test1234')
my_list.append('test12343344')
print(my_list)

numbers = [6,2,8,3,2]
numbers.sort()
print('numbers: {}'.format(numbers))

numbers.sort(reverse=True)
print('numbers: {}'.format(numbers))

words = ['thuis','is','a','of']
words.sort()
print('wiords: {}'.format(words))

hetro= ['2','9','3','word','is','a']
hetro.sort()
print('hetrod: {}'.format(hetro))
