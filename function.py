'''
def my_first_function():
    print('Hello World!')
print('type: {}'.format(my_first_function()))

my_first_function()

def my_first_function2(data1,data2):
    print('Hello {} {}'.format(data1,data2))
print('type: {}'.format(my_first_function2('case1','case2')))

my_first_function()


def strip_and_lowercase(original):
    modified = original.strip().lower()
    return modified

ugly_string = '  MiXeD CaSe'
print('result: {}'.format(strip_and_lowercase(ugly_string)))

def create_person_info(name,age,job=None,salary=3000):
    info = {'name':name,'age': age,'salary': salary}

    if job:
        info.update(dict(job=job))

    return info;

person1 = create_person_info('vinit',82)
person2 = create_person_info('Vinit2',22,'hacker',10000)
print(person1)
print(person2)


def my_fancy_calculation(first,second,third):
    return first +second - third

print(my_fancy_calculation(3,2,1))
print(my_fancy_calculation(first=3,second=2,third=1))

print(my_fancy_calculation(third=3,first=2,second=1))

print(my_fancy_calculation(3,third=1,second=2))

# print(my_fancy_calculation(3,first=1,second=2))

def printData(*names):
    print("type of passed argument is ",type(names))
    print("printing the passed arguments...")
    for name in names:
        print(name)

printData("vinit","kumar","1","2")
'''

def out_func():
    x=2
    print('x is',x)

    def inner_func():
        nonlocal x
        x=5
        print('x from inner function=',x)
    inner_func()
    print('x from outer function=',x)

out_func()

