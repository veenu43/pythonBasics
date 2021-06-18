'''
fileName = input("enter filename: ")
fileptr = open(fileName,"w")
fileptr.write("test line1.\n")
fileptr.write("test line2.\n")

str_list =['line1..\n','line2..\n']
fileptr.writelines(str_list)
fileptr.close()
print("Name of the file: ",fileptr.name)
print("Closed or not: ",fileptr.close())
print("Opening mode: ",fileptr.mode)

f = open("Test.txt")
data = f.read()
for ch in data:
    print(ch,end='')

position = f.tell();
f.seek(5)
data_line= f.readline()
'''
import pickle
shoplist = ['apple','mango','grape']
f = open('shoplist.txt','rb')
storedList = pickle.load(f)
print(storedList)
f.close()






