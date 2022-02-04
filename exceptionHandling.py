'''
i,j = 10,0
div = 0

def exceptTest(p,q):
    try:
        div = p / q
        print("Result: ",div)
    except ZeroDivisionError as ze:
        print(str(ze))

    except:
        print("Generic exception")

    finally:
        q=1

    return p,q

i,j = exceptTest(1,j)
print("i={},j={}".format(i,j))

'''
def acceptNumber():
    x= int(input('Enter Number'))
    if x<=0:
        raise Exception('Value should be greater than 0')
try:
    acceptNumber()
except Exception as ex:
    print(ex)



