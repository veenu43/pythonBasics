import csv
'''
import csv
products = [(1,'mobile',25000,10),(2,'laptop',50000,5),(3,'pen',25,100)]
csvfile=open("data.csv","w",newline='')
obj=csv.writer(csvfile)
for p in products:
    obj.writerow(p)
csvfile.close()


import csv
products = [(1,'mobile',25000,10),(2,'laptop',50000,5),(3,'pen',25,100)]
csvfile=open("data1.csv","w",newline='')
obj=csv.writer(csvfile)
obj.writerow(products)
csvfile.close()


import csv
csvfile=open("data.csv","r",newline='')
obj = csv.reader(csvfile)
for row in obj:
    print(row)
csvfile.close()

'''


employees = [{'name':'John','dept':'hr','salary':500000},
             {'name':'Mary','dept':'sales','salary':600000},
             {'name':'Peter','dept':'sales','salary':700000}]
fields = list(employees[0].keys())
csvfile = open('empData.csv','w',newline='')
obj=csv.DictWriter(csvfile,fieldnames=fields)
obj.writeheader()
obj.writerow(employees)
csvfile.close()


csvfile = open('empData.csv','r',newline='')
obj =csv.DictReader(csvfile)
for field in obj.fieldnames:
    print(field,end="\t")
print()
for row in obj:
    print(row)
csvfile.close();