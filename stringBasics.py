test='hello\
python\
you\
are\
dynamic'
print(test)


test1='''Welcome
to
the
world
of
python'''
print(test1)


print(len(test))
print(len(test1))

age=18
name='vinit'
#print(name + 'is' +age + 'years old')
print(name , 'is' ,age , 'years old')

print(name+ 'is'+ str(age)+'years old')
print("{0} is {1} years old".format(name,age))
print(" %s is %d years old"%(name,age))


message= "{} is of {} old"
print(message.format('vinit',18))


name="Vinit"
print(name[2:4])
print(name[2:5:2])

name1='vinit'
name2='kumar'
print(','.join([name1,name2]))

m="@@@@ Strin @@@hkhjk@@@"
print(m.strip('@@@'))
print(m.split('@@@'))

indented='\t This will be indented\t sdfsdf'
print(indented)

num1=input("num: ")
print(num1)